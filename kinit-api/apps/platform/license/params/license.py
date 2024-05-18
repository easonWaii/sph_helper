from fastapi import Depends, Query
from core.dependencies import Paging, QueryParams


class VLicenseParams(QueryParams):
    """
    授权码参数
    """
    def __init__(
            self,
            device_id: str | None = Query(None, title="角色名称"),
            license_key: str | None = Query(None, title="权限字符"),
            params: Paging = Depends()
    ):
        super().__init__(params)
        self.device_id = device_id
        self.license_key = license_key
