from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
import json
from core.crud import DalBase
from core.database import redis_getter
from core.exception import CustomException
from . import models, schemas
from typing import Any, Dict
from datetime import datetime
from application.settings import REDIS_DB_ENABLE
from redis.asyncio.client import Redis


class PlatformCookieDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(PlatformCookieDal, self).__init__()
        self.db = db
        self.model = models.PlatformCookie
        self.schema = schemas.CookieInfoPlatformCookieSimpleOut





    async def update_current_info(self, data: Dict[str,Any]) -> Any:
        """
        更新当前cookie对应的基本信息
        :param user:
        :param data:
        :return:
        """
        if data['session_id']:
            unique: models.PlatformCookie = await self.get_data(uniq_id=data['uniq_id'], v_return_none=True)
            if unique:
                unique.last_login_time.now()
            else:
                unique = self.model(**data)
            await self.flush(unique)
            return await self.out_dict(unique)
        else:
            raise CustomException("无cookie数据不可保存")

    # @staticmethod
    # async def set_cache_cookie(rd: Redis, data: schemas.PlatformCookie) -> Any:
    #     if REDIS_DB_ENABLE:
    #         await rd.client().set(data.uniq_id, json.dumps(data))
    #
    # @staticmethod
    # async def clear_cache_cookie(rd: Redis, uniq_id:str) -> Any:
    #     if REDIS_DB_ENABLE:
    #         await rd.client().delete(uniq_id)
    #
    # @staticmethod
    # async def get_cookie(rd: Redis, uniq_id: str) -> Any:
    #     if REDIS_DB_ENABLE:
    #         return await rd.client().get(uniq_id)
    #     return None



