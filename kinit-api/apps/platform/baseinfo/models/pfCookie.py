from sqlalchemy.orm import Mapped, mapped_column
from db.db_base import BaseModel
from sqlalchemy import String, Boolean, Integer, ForeignKey, DateTime, func
from datetime import datetime


class PlatformCookie(BaseModel):
    __tablename__ = "platform_baseinfo_cookie"
    __table_args__ = ({'comment': 'cookie表'})

    uniq_id: Mapped[str] = mapped_column(String(50), index=True, nullable=False, comment="平台标识id")
    nick_name: Mapped[str] = mapped_column(String(50), index=True, nullable=False, comment="昵称")
    finder_name: Mapped[str] = mapped_column(String(255), index=True, nullable=True, comment="finder_name")
    session_id: Mapped[str] = mapped_column(String(255), index=True, nullable=True, comment="session_id")
    platform_name: Mapped[str] = mapped_column(String(50), index=True, nullable=True, comment="平台名称")
    head_img_url: Mapped[str] = mapped_column(String(255), index=True, nullable=False, comment="头像url")
    last_login_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment='最近访问时间')



