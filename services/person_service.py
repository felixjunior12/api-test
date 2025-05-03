from schemas.person_schema import PersonSchema, PersonCreateSchema
from services import country_service
from db.db import get_db_pool


async def create_person(data):
    pool = get_db_pool()
    country_id = await country_service.get_country_id_or_create(data.birth_country.capitalize())
    async with pool.acquire() as conn:
        await conn.execute("""
            INSERT INTO person (first_name, last_name, passport_number, birth_date, birth_country)
            VALUES ($1, $2, $3, $4, $5)
        """, data.first_name, data.last_name, data.passport_number, data.birth_date, country_id)


async def get_person(id):
    pool = get_db_pool()
    async with pool.acquire() as conn:
        result = await conn.fetch("SELECT p.id, p.first_name, p.last_name, p.passport_number, p.birth_date, c.name as birth_country FROM person as p INNER JOIN country as c ON p.birth_country = c.id WHERE p.id = $1", id)
        return PersonSchema(**result[0]) if result else None


async def update_person(id, data):
    pool = get_db_pool()
    country_id = await country_service.get_country_id_or_create(data.birth_country.capitalize())
    async with pool.acquire() as conn:
        await conn.execute("""
            UPDATE person SET first_name = $1, last_name = $2, passport_number = $3, birth_date = $4, birth_country = $5 WHERE id = $6
        """, data.first_name, data.last_name, data.passport_number, data.birth_date, country_id, id)


async def delete_person(id):
    pool = get_db_pool()
    async with pool.acquire() as conn:
        await conn.execute("DELETE FROM person WHERE id = $1", id)


async def get_persons():
    pool = get_db_pool()
    async with pool.acquire() as conn:
        result = await conn.fetch("SELECT p.id, p.first_name, p.last_name, p.passport_number, p.birth_date, c.name as birth_country FROM person as p INNER JOIN country as c ON p.birth_country = c.id ")
        return [PersonSchema(**row) for row in result]