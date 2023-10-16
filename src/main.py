from fastapi import FastAPI
from .schema import Pet, PetResponse
from uuid import UUID

app = FastAPI()


@app.post("/pet", status_code = 201)
def post_pet(pet: Pet) -> PetResponse:
    pass

@app.get("/pet", status_code = 200)
def get_pets(skip: int = 0, limit: int = 0, order: str | None = None) -> list[Pet]:
    pass

@app.get("/pet/{pet_id}", status_code = 201)
def get_pets_by_id(
    pet_id: UUID
) -> Pet:
    pass

@app.put("/pet/{pet_id}", status_code = 202)
def update_pet(
    pet_id: UUID,
    pet: Pet
) -> Pet:
    pass

@app.delete("/pet/{pet_id}", status_code = 203)
def delete_pet(
    pet_id: UUID
) -> None:
    pass