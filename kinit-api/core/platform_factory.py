from request.platform_factory import PlatformFactory
from fastapi import Request


def platform_factory_getter(db, request: Request) -> PlatformFactory:
    """
    获取 ABC类的实体
    全局挂载，使用一个工厂对象
    """
    return request.app.state.platform_factory(db, request.body())
