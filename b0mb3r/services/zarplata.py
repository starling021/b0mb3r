from service import Service


class Zarplata(Service):
    async def run(self):
        await self.post(
            "https://hr.zarplata.ru/api/v2/users",
            json={
                "phone": {"value": self.formatted_phone},
                "password": self.password,
                "type": "employer",
            },
        )
