from b0mb3r.services.service import Service


class Hmara(Service):
    async def run(self):
        await self.get(
            "https://my.hmara.tv/api/sign", params={"contact": self.formatted_phone},
        )
