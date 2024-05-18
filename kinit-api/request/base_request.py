from abc import ABC, abstractmethod
from typing import Dict, Optional


class AbstractClient(ABC):

    @abstractmethod
    async def set_init(self, session_id, db, default_get=False):
        pass

    @abstractmethod
    async def get_base_info(self):
        pass

    @abstractmethod
    async def get_video_list(self, page_size, offset, start_time: str, end_time: str):
        pass

    @abstractmethod
    async def pong(self, session_id):
        pass

    @abstractmethod
    async def _update_cookie(self, db):
        pass

    @abstractmethod
    async def request(self, method, url, **kwargs):
        pass

    @abstractmethod
    async def get_over_threshold_list(self, keywords, start_time, end_time):
        pass
