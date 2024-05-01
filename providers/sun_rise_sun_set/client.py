import os
import signal
from dataclasses import dataclass

import httpx


@dataclass
class SunRiseInfo(object):
    sun_rise_time: str
    date: str


class SunRiseClient(object):

    time_format = "%I:%M:%S %p"

    def __init__(self, url):
        self._client = httpx.AsyncClient(base_url=url)

    async def get_sunrise(
        self,
        latitude,
        longitude,
        date,
    ) -> SunRiseInfo:
        try:
            response = await self._client.get(
                url="json",
                params={
                    "lat": latitude,
                    "lng": longitude,
                    "date": date,
                },
            )
        except httpx.ConnectError:
            os.kill(os.getpid(), signal.SIGTERM)
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError:
            os.kill(os.getpid(), signal.SIGABRT)

        response_data = response.json()
        return SunRiseInfo(
            sun_rise_time=response_data["results"]["sunrise"],
            date=response_data["results"]["date"],
        )
