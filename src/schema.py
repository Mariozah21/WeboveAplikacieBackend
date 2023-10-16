from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, date

class Owner(BaseModel):
    name: str


class MedicalExamination(BaseModel):
    date_time: datetime
    doctor: str
    report: str

class Pet(BaseModel):
    id: UUID
    name: str
    birthday: date
    kind: str
    owner: Owner
    medical_exams: list[MedicalExamination]

class PetResponse(BaseModel):
    pet: Pet

class PetSliceResponse(BaseModel):
    pets: Pet
    current: int
    limit: str