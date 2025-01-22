from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer


class Base(DeclarativeBase):
    __tablename__ = __name__
    id = Column(Integer, primary_key=True)


class Metizes(Base):
    number_in_catalog = Column(String, default='-')
    number_in_catalog_agb = Column(String, default='-')
    name_in_catalog = Column(String, default='-')
    name_in_kd = Column(String, default='-')
    name_in_catalog_agb = Column(String, default='-')
    standard = Column(String, default='-')
    type = Column(String, default='-')
    profile = Column(String, default='-')
    diameter_nominal = Column(String, default='-')
    step = Column(String, default='-')
    length = Column(String, default='-')
    accuracy = Column(String, default='-')
    material_or_coverage = Column(String, default='-')
    assigned = Column(String, default='-')
    note = Column(String, default='-')
    applicability = Column(String, default='-')
    date = Column(String, default='-')
