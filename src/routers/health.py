from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/health")
async def ping() -> JSONResponse:
    """
    Endpoint for basic health check.
    :return: A JSON response containing a message indicating the server's status.
    """
    content = {"message": "Ok"}
    return JSONResponse(content=content)
