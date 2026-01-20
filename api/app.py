from fastapi import FastAPI
from api.routes import routers
from starlette.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware


args = {"host": "127.0.0.1", "port": 8080}


app = FastAPI()
# add
app.include_router(route)

class RedirectToDocs(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path == "/":
            return RedirectResponse(url="/docs")
        response = await call_next(request)
        return response


app.add_middleware(RedirectToDocs)