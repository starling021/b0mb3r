from b0mb3r.services.service import Service


class Cian(Service):
    async def run(self):
        await self.post(
            "https://api.cian.ru/sms/v2/send-validation-code/",
            json={"phone": "+" + self.formatted_phone, "type": "authenticateCode"},
        )
