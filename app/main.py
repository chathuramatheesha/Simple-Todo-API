from fastapi import FastAPI

from app import api
from app.db.database import Base, engine
from app.core.config import settings

app = FastAPI()

app.include_router(api.router, prefix="/api")


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def startup():
    print("Starting the server...")
    print("Initializing the database")
    await init_db()
    print("Initialize Completed")


async def shutdown():
    print("Shutting Down the server...")


app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=True)
