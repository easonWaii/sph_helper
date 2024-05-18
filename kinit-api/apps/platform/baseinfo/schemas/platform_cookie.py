from pydantic import BaseModel, ConfigDict
from core.data_types import DatetimeStr


class PlatformCookie(BaseModel):
    uniq_id: str | None = ''
    nick_name: str | None = ''
    finder_name: str | None = 'null'
    session_id: str
    platform_name: str | None = 'wx_sph'
    head_img_url: str | None = None
    last_login_time: DatetimeStr | None = None


class CookieInfoPlatformCookieSimpleOut(PlatformCookie):
    model_config = ConfigDict(from_attributes=True)

    id: int
    create_datetime: DatetimeStr
    update_datetime: DatetimeStr


class FrontPlatformCookie(BaseModel):
    uniq_id: str | None = ''
    session_id: str
    platform_name: str | None = 'wx_sph'


