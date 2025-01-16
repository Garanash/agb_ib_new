from pydantic import BaseModel, ConfigDict


class MetizBase(BaseModel):
    id: int
    number_in_catalog: str
    number_in_catalog_agb: str
    name_in_catalog: str
    name_in_kd: str
    name_in_catalog_agb: str
    standard: str
    type: str
    profile: str | None
    diameter_nominal: str
    step: str
    length: str
    accuracy: str
    material_or_coverage: str
    assigned: str
    note: str
    applicability: str
    date: str


class MetizCreate(MetizBase):
    pass


class MetizUpdate(MetizCreate):
    pass


class MetizUpdatePartial(MetizCreate):
    number_in_catalog: str | None = None
    number_in_catalog_agb: str | None = None
    name_in_catalog: str | None = None
    name_in_kd: str | None = None
    name_in_catalog_agb: str | None = None
    standard: str | None = None
    type: str | None = None
    profile: str | None = None
    diameter_nominal: str | None = None
    step: str | None = None
    length: str | None = None
    accuracy: str | None = None
    material_or_coverage: str | None = None
    assigned: str | None = None
    note: str | None = None
    applicability: str | None = None
    date: str | None = None


class Metiz(MetizBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
