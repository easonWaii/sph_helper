from fastapi import Depends, Query, Body
from core.dependencies import Paging, QueryParams


class PlatformAccountParams(QueryParams):
    """
    列表分页
    """

    def __init__(
            self,
            session_id: str | None = Body(None, title="会话ID"),
            platform_name: str | None = Body(None, title="平台名称"),
            params: Paging = Depends()
    ):
        super().__init__(params)
        self.session_id = session_id
        self.platform_name = ("like", platform_name)
