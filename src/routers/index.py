"""
ping router for pseudo health check
"""

from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/index")
async def index():
    content = {"result": "success", "message": "Hi from coffe-shopp"}
    return JSONResponse(content=content)
