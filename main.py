# Аренда облачного сервиса: https://selectel.ru/services/cloud/servers/?section=about&utm_source=youtube.com&utm_medium=referral&utm_campaign=help_cloud_sharedline_13022024_shumeiko_paid
import uvicorn
from fastapi import FastAPI
from api.routes import router as api_router
from core.config import settings

app = FastAPI()
app.include_router(
    api_router,
    prefix=settings.api.prefix
)


if __name__ == "__main__":
    uvicorn.run("main:app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)