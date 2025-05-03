from db.db import get_db_pool


async def create_country(name):
    pool = get_db_pool()
    async with pool.acquire() as conn:
        await conn.execute("INSERT INTO country (name) VALUES ($1)", name)

async def get_country(id):
    pool = get_db_pool()
    async with pool.acquire() as conn:
        result = await conn.fetch("SELECT * FROM country WHERE id = $1", id)
        return result[0]

async def update_country(id, name):
    pool = get_db_pool()
    async with pool.acquire() as conn:
        await conn.execute("UPDATE country SET name = $1 WHERE id = $2", name, id)

async def delete_country(id):
    pool = get_db_pool()
    async with pool.acquire() as conn:
        await conn.execute("DELETE FROM country WHERE id = $1", id)

async def get_countries():
    pool = get_db_pool()
    async with pool.acquire() as conn:
        result = await conn.fetch("SELECT * FROM country")

async def get_country_by_name(name):
    pool = get_db_pool()
    async with pool.acquire() as conn:
        result = await conn.fetch("SELECT * FROM country WHERE name = $1", name)
        return result[0] if result else None

async def get_country_id_or_create(name):
    country = await get_country_by_name(name)
    if not country:
        await create_country(name)
        country = await get_country_by_name(name)
    return country['id'] if country else None

