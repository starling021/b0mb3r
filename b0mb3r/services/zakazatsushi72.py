from b0mb3r.services.service import Service


class ZakazatSushi72(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax.php?do=sms_code",
            data={"phone": self.format(self.phone, "8(***)***-**-**")},
        )
