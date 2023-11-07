"""
Main module for configuring and running the API server.

Refer to README.rst for instructions to run the server.

:see: https://fastapi.tiangolo.com/tutorial/bigger-applications/
"""
__all__ = ["app"]

import asyncio

import uvloop
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .routers import v1

# Activate uvloop for improved asyncio performance.
# :see: https://uvloop.readthedocs.io/
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# Initialise the FastAPI application.
app = FastAPI()

# Register routers to serve the API endpoints.
app.include_router(v1.router)


@app.get("/")
def homepage() -> RedirectResponse:
    """
    Redirects ``/`` to ``/v1``.
    """
    return RedirectResponse("/v1")
