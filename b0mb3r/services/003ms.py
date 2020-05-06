from service import Service


class Ms003(Service):
    async def run(self):
        await self.post(
            "https://003ms.ru/auth/register", data={"phone": self.formatted_phone, "ajax": 1},
        )
