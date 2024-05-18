from fastapi import Body

from request.base_request import AbstractClient
from request.platform.wx_shp import WxSphClient


class PlatformFactory:
    _instance = {}

    def __call__(self, platform_name: str = Body(...), session_id: str = Body(...)) -> AbstractClient:
        if platform_name not in self._instance:
            if platform_name == "wx_sph":
                self._instance[platform_name] = WxSphClient()
            else:
                raise ValueError(f"Invalid product name: {platform_name}")
        # self._instance[platform_name].set_init(session_id, db)
        return self._instance[platform_name]
