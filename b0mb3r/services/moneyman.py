from service import Service


class MoneyMan(Service):
    async def run(self):
        await self.post(
            "https://moneyman.ru/registration_api/actions/send-confirmation-code",
            data="+" + self.formatted_phone,
        )
