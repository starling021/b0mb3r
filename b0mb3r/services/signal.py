from b0mb3r.services.service import Service


class Signal(Service):
    async def run(self):
        await self.post(
            "https://deathstar.signal.is/auth",
            data={"phone": "+" + self.formatted_phone},
        )
