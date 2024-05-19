from fastapi import APIRouter, Depends, HTTPException
from core.platform_factory import platform_factory_getter
from request.base_request import AbstractClient
from utils.response import SuccessResponse

from apps.vadmin.auth.utils.current import FullAdminAuth
from apps.vadmin.auth.utils.validation.auth import Auth
from .crud import VLicenseDal
from .params.license import VLicenseParams
from starlette import status
from .schemas import VLicense

app = APIRouter()


@app.post("license/verify_update/", summary="post设备码与license验证并更新")
async def verify_and_store_license(data: VLicense, auth: Auth = Depends(FullAdminAuth())):
    res_data = await VLicenseDal(auth.db).verify_license_and_store(data)
    return SuccessResponse(res_data)


@app.post("/license/verify", summary="以设备码验证")
async def verify(data: VLicense, auth: Auth = Depends(FullAdminAuth())):
    res_data = await VLicenseDal(auth.db).verify_by_device_id(data.device_id)
    return SuccessResponse(res_data)
