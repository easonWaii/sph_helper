from datetime import datetime
from typing import Any, Dict

from sqlalchemy.ext.asyncio import AsyncSession
from core.crud import DalBase
from . import models, schemas
from .utils.auth_license import decode_license


class VLicenseDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(VLicenseDal, self).__init__()
        self.db = db
        self.model = models.VLicense
        self.schema = schemas.VLicenseSampleOut

    async def verify_license_and_store(self, license_obj: schemas.VLicense) -> Dict[str, Any]:
        try:
            status_code = decode_license(license_obj.device_id, license_obj.license_key)
            if status_code == -1:
                return {"status": -1, "message": "授权码与设备不匹配"}
            elif status_code == 0:
                return {"status": -1, "message": "授权过期"}

            # 检查数据库中是否已有该设备ID，有就更新，没有就新增
            db_license = await self.get_data(v_where=[self.model.device_id == license_obj.device_id])
            if db_license:
                db_license.license_key = license_obj.license_key
                await self.flush(db_license)
            else:
                await self.create_data(license_obj)

            return {"status": 0, "message": "授权码有效"}
        except Exception as e:
            return {"status": -1, "message": str(e)}

    async def verify_by_device_id(self, device_id: str) -> Dict[str, Any]:
        db_license = await self.get_data(v_where=[self.model.device_id == device_id])
        if not db_license:
            return {"status": -1, "message": "该设备未被授权"}
        # 解码授权码，验证码是否过期，并且是否是与本机匹配的
        decoded_device_id, expire_time = decode_license(db_license.license_key)
        if device_id != decoded_device_id:
            return {"status": -1, "message": "该授权码与设备不匹配"}
        if datetime.now().timestamp() > expire_time:
            return {"status": -1, "message": "授权过期"}
