from fastapi import Depends, Query, Body
from core.dependencies import Paging, QueryParams


class VideoInfoParams(QueryParams):
    """
    视频信息分页
    """

    def __init__(
            self,
            session_id: str | None = Body(None, title="会话ID"),
            start_time: str | None = Body(None, title='start_time'),
            end_time: str | None = Body(None, title='end_time'),
            params: Paging = Depends()
    ):
        super().__init__(params)
        self.session_id = session_id
        self.start_time = start_time
        self.end_time = end_time
