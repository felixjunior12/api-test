import asyncpg
from fastapi import FastAPI

# Este módulo tendrá una única instancia del pool
db_pool = None

async def init_db_pool(app: FastAPI):
    global db_pool
    db_pool = await asyncpg.create_pool(
        dsn="postgresql://fmicolta:WhXFjU1XZHwPkdq7ffv1nBhDtfQNcYUQ@dpg-d0a53qbuibrs73ats3kg-a.oregon-postgres.render.com/test_db_name_667o",
        min_size=5,
        max_size=20
    )
    print("✅ ¡Conexión exitosa!")
    app.state.db_pool = db_pool

async def close_db_pool():
    await db_pool.close()

def get_db_pool():
    return db_pool