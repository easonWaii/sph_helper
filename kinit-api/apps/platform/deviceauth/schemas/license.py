from pydantic import BaseModel, ConfigDict
from core.data_types import DatetimeStr


class VLicense(BaseModel):
    device_id: str
    license_key: str | None = None


class VLicenseSampleOut(VLicense):
    model_config = ConfigDict(from_attributes=True)

    id: int
    create_datetime: DatetimeStr
    update_datetime: DatetimeStr
