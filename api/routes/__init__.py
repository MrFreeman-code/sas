from fastapi import APIRouter, Depends
from fastapi.openapi.docs import get_swagger_ui_html


from fastapi import APIRouter

from api.routes.auth import router as auth_router
from api.routes.dtt import router as dtt_router

routers = APIRouter()

routers.include_router(auth_router)
routers.include_router(task_router)


# @routers.get(
#     "/openapi/scheme",
#     include_in_schema=False
# )
# async def get_documentation():
#     return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")
