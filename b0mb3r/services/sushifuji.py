from b0mb3r.services.service import Service


class SushiFuji(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://sushifuji.ru/sms_send_ajax_sms.php",
            data={"name_sms": "false", "phone_sms": self.formatted_phone},
        )
