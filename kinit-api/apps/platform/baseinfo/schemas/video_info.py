from pydantic import BaseModel, ConfigDict
from core.data_types import DatetimeStr


class VideoInfo(BaseModel):
    session_id: str | None = ''
    start_time: DatetimeStr | None = None
    end_time: DatetimeStr | None = None


class VideoInfoSimpleOut(VideoInfo):
    model_config = ConfigDict(from_attributes=True)

    id: int
    create_datetime: DatetimeStr
    update_datetime: DatetimeStr


