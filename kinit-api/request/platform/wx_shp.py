import json
import time
from typing import Dict, Union, Any, Optional, List

import httpx

from httpx import RequestError
from motor.core import AgnosticDatabase
from motor.motor_asyncio import AsyncIOMotorDatabase

from redis.asyncio.client import Redis
from datetime import datetime
from apps.platform.baseinfo.crud import PlatformCookieDal
from apps.platform.baseinfo.schemas import PlatformCookie
from request.base_request import AbstractClient
from utils.request_util import get_user_agent
from application.request_config import wx_sph
from utils.tools import get_datetime_timestamp, filter_dict_optimized


class WxSphClient(AbstractClient):
    def __init__(self, timeout=10):

        self.timeout = timeout
        self.headers = {'User-Agent': get_user_agent(),
                        'Accept': 'application/json, text/plain, */*',
                        'Content-Type': 'application/json;charset=UTF-8'
                        }
        self.union_id = ''
        self.session_id = ''
        self.finder_id = 'null'
        self._host = wx_sph.BASE_URL
        # finder_id与request_body应该去redis缓存中找，如果没有，则新建

    async def set_init(self, session_id: str, db: AgnosticDatabase, default_get: bool = False) -> Optional[
        dict[str, Any]]:
        if self.session_id == session_id or not session_id:
            return None
        self.session_id = session_id
        data = await self.get_base_info()
        self.union_id = data['union_id']
        self.finder_id = data['finder_id']
        # 当session_id不同时，更新数据库数据
        await self._update_cookie(db)
        db = None
        if default_get:
            return data
        return None

    @staticmethod
    def _get_request_body() -> Dict[str, str]:
        return {
            "timestamp": time.time() * 1000,
            "_log_finder_id": "null",
            "rawKeyBuff": "null"
        }

    def _get_request_body_with_pagination(self, page_size: int, offset: int, start_time: str, end_time: str) -> Dict[
        str, str]:
        return {
            "timestamp": time.time() * 1000,
            "_log_finder_id": self.finder_id,
            "rawKeyBuff": "null",
            "currentPage": offset + 1,
            "pageSize": page_size,
            "startTime": get_datetime_timestamp(start_time),
            "endTime": get_datetime_timestamp(end_time)
        }

    def _get_cookies(self) -> Dict[str, str]:
        return {'sessionid': self.session_id}

    async def _update_base_info(self, data: Dict[str, Any], db: AsyncIOMotorDatabase):
        await PlatformCookieDal(db).update_current_info(data)

    async def request(self, method, url, **kwargs) -> Union[str, Any]:
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method, url, timeout=self.timeout,
                headers=self.headers,
                cookies=self._get_cookies(),
                **kwargs
            )
        data: Dict = response.json()
        if data["errCode"] == 0:
            return data.get("data", {})
        elif data["errCode"] == 300333:
            # 发生错误300333错误时，为cookie失效，清除cache中的sessionid

            raise RequestError('cookie已失效')
        else:
            raise RequestError(data.get("errMsg", ''))

    async def get_base_info(self) -> Dict[str, Any]:
        """
        返回sph用户的基本信息情况
        """
        base_info_url = wx_sph.BASE_INFO_URL
        res_data = await self.request('POST', base_info_url, data=self._get_request_body())
        res_data = json.loads(res_data)
        find_user = res_data['finderUser']
        self.finder_id = find_user['finderUsername']
        self.union_id = find_user['uniqId']

        response_data = {
            'uniq_id': find_user['uniqId'],
            'nick_name': find_user['nickname'],
            'head_img_url': find_user['headImgUrl'],
            'finder_id': find_user['finderUsername'],
            'feeds_count': res_data['feedsCount'],
            'fans_count': res_data['fansCount'],
            'session_id': self.session_id,
            'platform_name': 'wx_sph'
        }
        return response_data

    async def get_video_list(self, page_size: int, offset: int, start_time: str, end_time: str) -> (List[Any], int):
        """
        获取指定范围内的视频数据列表
        :param page_size:分页大小
        :param offset:页码偏移
        :param start_time:开始查询时间
        :param end_time:截止时间
        :return dict 原封返回，后期可能有字段增加，暂以原封返回的方式
        """
        video_list_url = wx_sph.VIDEO_LIST_URL
        body_data = self._get_request_body_with_pagination(page_size, offset, start_time, end_time)
        res_data = await self.request('POST', video_list_url, data=body_data)
        res_data = json.loads(res_data)
        return res_data['data']['list'], res_data['data']['totalCount']

    async def get_over_threshold_list(self, keywords: Union[Dict[str, int], str], start_time: str, end_time: str) -> (
    List[Any], int):
        """
        按照keywords里面的关键字及阈值，对时间区间内的相关数据进行提取
        :param keywords:dict「关键字:阈值」，后期可能有多关键字报警的需求
        :return:dict
        """
        if isinstance(keywords, str):
            keywords = json.loads(keywords)
        data = await self.get_video_list(1000, 0, start_time, end_time)
        data = filter_dict_optimized(data, keywords)
        return data, len(data)

    async def pong(self, session_id):
        request_url = wx_sph.HEART_BEAT_URL
        self.session_id = session_id
        res_data = await self.request('POST', request_url, data=self._get_request_body())
        res_data = json.loads(res_data)
        if res_data['errCode'] == 0:
            return {'status': 1}
        else:
            return {'status': 0}

    # update cookie info and update to database
    # return base_info
    async def _update_cookie(self, db: AgnosticDatabase, data=None):
        if data is None:
            data = await self.get_base_info()
        await self._update_base_info(data, db)
        return data
