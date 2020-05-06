from service import Service


class AptekaOnline(Service):
    async def run(self):
        await self.post(
            "https://www.aptekaonline.ru/login/ajax_sms_order.php",
            data={"PERSONAL_MOBILE": "+" + self.formatted_phone},
        )
