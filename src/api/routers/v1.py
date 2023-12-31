"""
Define routes for our v1 API.
"""
__all__ = ["router"]

from fastapi import APIRouter

# All API routes defined in this module will have a path prefix of ``/v1``.
# E.g., ``@router.get("/foo/bar")`` adds a route at ``/v1/foo/bar``.
# :see: https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter
router = APIRouter(prefix="/v1", tags=["v1"])


@router.get("/")
def index() -> dict:
    """
    Simple static route, so that we can confirm the server is running.
    """
    return {"message": "Kia ora te ao!"}
