import json

from b0mb3r.services.service import Service


class SauiriSushi(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://api.saurisushi.ru/Sauri/api/v2/auth/login",
            data={"data": json.dumps({"login": self.phone})},
        )
