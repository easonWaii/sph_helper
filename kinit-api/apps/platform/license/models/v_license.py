
from db.db_base import BaseModel
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class VLicense(BaseModel):
    __tablename__ = "platform_license_vlicense"
    __table_args__ = ({'comment': 'license表'})

    device_id: Mapped[str] = mapped_column(String(255), comment="设备id")
    license_key: Mapped[str | None] = mapped_column(String(255), comment="许可证key")




