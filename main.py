# Аренда облачного сервиса: https://selectel.ru/services/cloud/servers/?section=about&utm_source=youtube.com&utm_medium=referral&utm_campaign=help_cloud_sharedline_13022024_shumeiko_paid
import uvicorn
from fastapi import FastAPI
from core.config import settings
from contextlib import asynccontextmanager
from api.routes import router as api_router
from core.db.pg.base import db_session_manager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # strtup
    yield
    # shutdown
    await db_session_manager.dispose()


app = FastAPI(
    lifespan=lifespan
)
app.include_router(
    api_router,
    prefix=settings.api.prefix
)


if __name__ == "__main__":
    uvicorn.run("main:app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)