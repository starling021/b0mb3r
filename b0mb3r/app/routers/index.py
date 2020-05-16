import os
from os.path import join

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from loguru import logger

from b0mb3r.service import services

router = APIRouter()
templates = Jinja2Templates(directory=join(os.getcwd(), "app", "templates"))


@logger.catch
@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "service_count": len(services[7])}
    )
