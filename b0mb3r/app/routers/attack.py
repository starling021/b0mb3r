import asyncio
import re
import uuid

import phonenumbers
from fastapi import APIRouter, HTTPException
from loguru import logger

from b0mb3r.app.models import AttackModel, StatusModel
from b0mb3r.app.status import status
from b0mb3r.main import perform_attack

router = APIRouter()


@logger.catch
@router.post("/start")
async def start_attack(attack: AttackModel):
    only_digits_phone = re.sub("[^0-9]", "", attack.phone)
    country_code = phonenumbers.parse(f"+{only_digits_phone}").country_code

    attack_id = uuid.uuid4().hex
    status[attack_id] = {"started_at": None, "currently_at": None, "end_at": None}

    asyncio.create_task(
        perform_attack(attack_id, attack.number_of_cycles, country_code, only_digits_phone)
    )

    return {"success": True, "id": attack_id}


@logger.catch
@router.get("/{attack_id}/status", response_model=StatusModel)
def get_attack_status(attack_id: str):
    if attack_id not in status:
        raise HTTPException(status_code=404)
    return StatusModel(**status[attack_id])
