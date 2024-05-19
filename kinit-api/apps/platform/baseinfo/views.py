from fastapi import APIRouter, Depends, HTTPException
from core.platform_factory import platform_factory_getter
from request.base_request import AbstractClient
from utils.response import SuccessResponse

from apps.vadmin.auth.utils.current import FullAdminAuth
from apps.vadmin.auth.utils.validation.auth import Auth
from .crud import PlatformCookieDal
from .params.baseinfo import BaseInfoParams
from .params.over_threshold import OverThresholdParams
from .params.platform_account import PlatformAccountParams
from .params.video_info import VideoInfoParams
from starlette import status

from .schemas import PlatformCookie,VideoInfo

app = APIRouter()

@app.post("/platform/baseinfo", summary="获取cookie相关的基本信息")
async def get_base_info(data: PlatformCookie, auth: Auth = Depends(FullAdminAuth()),
                        platform_client: any = Depends(platform_factory_getter)):
    if isinstance(platform_client, AbstractClient):
        res_data = await platform_client.set_init(data.session_id, auth.db)
        if not res_data:
            res_data = await platform_client.get_base_info()
        return SuccessResponse(data=res_data)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.post("/platform/videoinfos", summary="获取平台账号相关的视频列表")
async def get_video_infos(data: VideoInfoParams = Depends(), auth: Auth = Depends(FullAdminAuth()),
                          platform_client: any = Depends(platform_factory_getter)):
    if isinstance(platform_client, AbstractClient):
        data_list, count = await platform_client.get_video_list(data.limit, data.page, data.start_time, data.end_time)
        return SuccessResponse(data=data_list, count=data)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.post("/platform/overthresholdvideo", summary="获取平台视频作品超阈值数的列表")
async def get_video_over_threshold(data: OverThresholdParams = Depends(), auth: Auth = Depends(FullAdminAuth()),
                          platform_client: any = Depends(platform_factory_getter)):
    if isinstance(platform_client, AbstractClient):
        data_list, count = await platform_client.get_over_threshold_list(data.keywords, data.start_time, data.end_time)
        return SuccessResponse(data=data_list, count=data)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/platform/account", summary="获取平台账号相关的视频列表")
async def get_accounts(params: PlatformAccountParams = Depends(), auth: Auth = Depends(FullAdminAuth())):
    datas, count = await PlatformCookieDal(auth.db).get_datas(**params.dict(), v_return_count=True)


@app.post("/platform/account", summary="登陆态验证")
async def check_status_info(data: BaseInfoParams = Depends(), auth: Auth = Depends(FullAdminAuth()),
                            platform_client: any = Depends(platform_factory_getter)):
    if isinstance(platform_client, AbstractClient):
        res_data = await platform_client.pong(data.session_id)
        return SuccessResponse(data=res_data)
