from b0mb3r.services.service import Service


class Apteka(Service):
    async def run(self):
        await self.post(
            "https://api.apteka.ru/auth/auth_code",
            json={"phone": "+" + self.formatted_phone, "cityId": "5e57803249af4c0001d64407"},
        )
