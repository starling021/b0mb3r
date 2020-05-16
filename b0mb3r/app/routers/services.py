from typing import Union

from fastapi import APIRouter
from loguru import logger

from b0mb3r.service import services

router = APIRouter()


@logger.catch
@router.get("/count")
def get_services_count(
    country_code: Union[int, str]  # It will be str if "Not listed" country is selected in frontend
):
    if country_code in services:
        return {"count": len(services[country_code])}
    return {"count": len(services["other"])}
