from pydantic import BaseModel


class MetizBase(BaseModel):
    id: int
    number_in_catalog: str
    number_in_catalog_agb: str
    name_in_catalog: str
    name_in_kd: str
    name_in_catalog_agb: str
    standard: str
    type: str
    profile: str
    diameter_nominal: str
    step: str
    length: str
    accuracy: str
    material_or_coverage: str
    assigned: str
    note: str
    applicability: str
    date: str
