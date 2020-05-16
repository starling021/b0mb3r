import os
from os.path import join

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from b0mb3r.app.routers import attack, services, index
from b0mb3r.utils import retrieve_installed_version

app = FastAPI(title="b0mb3r", version=retrieve_installed_version())

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=join(os.getcwd(), "app", "static")), name="static")

app.include_router(attack.router, prefix="/attack", tags=["attack"])
app.include_router(services.router, prefix="/services", tags=["services"])
app.include_router(index.router)
