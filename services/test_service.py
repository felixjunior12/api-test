from db.db import get_db_pool

async def get_all_users():
    pool = get_db_pool()
    async with pool.acquire() as connection:
        rows = await connection.fetch("SELECT id, name FROM users")
        return [dict(row) for row in rows]