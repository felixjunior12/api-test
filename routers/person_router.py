from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.person_schema import PersonCreateSchema, PersonSchema, PersonCreatedResponseSchema
from services import person_service


router = APIRouter(prefix="/person", tags=["Persons"])


@router.post("/", response_model=PersonCreatedResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_person(person: PersonCreateSchema):
    try:
        await person_service.create_person(person)
        return PersonCreatedResponseSchema(message="Person created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{id}", response_model=PersonSchema, status_code=status.HTTP_200_OK)
async def get_person(id: int):
    person = await person_service.get_person(id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@router.get("/", response_model=List[PersonSchema], status_code=status.HTTP_200_OK)
async def get_persons():
    persons = await person_service.get_persons()
    return persons


@router.put("/{id}", response_model=PersonCreatedResponseSchema, status_code=status.HTTP_200_OK)
async def update_person(id: int, person: PersonCreateSchema):
    try:
        await person_service.update_person(id, person)
        return PersonCreatedResponseSchema(message="Person updated")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{id}", response_model=PersonCreatedResponseSchema, status_code=status.HTTP_200_OK)
async def delete_person(id: int):
    try:
        await person_service.delete_person(id)
        return PersonCreatedResponseSchema(message="Person deleted")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

