from service import Service


class NaPopravku(Service):
    async def run(self):
        await self.post(
            "https://napopravku.ru/api/v2/user/send/sms/",
            data={"phone": "+" + self.formatted_phone, "onlyAuth": 0},
        )
