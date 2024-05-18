from typing import Dict

from fastapi import Depends, Query, Body
from core.dependencies import Paging, QueryParams


class OverThresholdParams(QueryParams):
    """
    视频超阈值信息返回
    keywords: Dict[str, int], start_time: str, end_time: str
    """
    def __init__(
            self,
            session_id: str | None = Body(None, title="会话ID"),
            keywords: Dict[str, int] | None = Body(None, title='筛选字段及阈值'),
            start_time: str | None = Body(None,title='start_time'),
            end_time: str | None = Body(None, title='end_time'),
            params: Paging = Depends()
    ):
        super().__init__(params)
        self.session_id = session_id
        self.keywords = keywords
        self.start_time = start_time
        self.end_time = end_time
