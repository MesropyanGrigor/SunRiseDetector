import argparse
import asyncio
import datetime
import logging
import signal
import sys
from collections.abc import Sequence

import handlers
from providers.coordinates.client import CountryCoordinatesClient
from providers.sun_rise_sun_set.client import SunRiseClient

logger = logging.getLogger("SUN RISE")
logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)

format = "%I:%M %p"


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="Sun Rise Detector",
        description="Find Sun Rise Day by the time",
    )
    parser.add_argument(
        "--country",
        action="store",
        help="Country name",
        required=True,
    )
    parser.add_argument(
        "--sun_rise_time",
        action="store",
        help="The time when sun will be risen, (ex. 06:30 AM)",
        required=True,
    )

    args = parser.parse_args(argv)
    try:
        sun_rise_time = datetime.datetime.strptime(args.sun_rise_time, format)
        args.sun_rise_time = sun_rise_time
    except ValueError:
        logger.error(" --sun_rise_time option is given in wrong format")
        parser.print_usage()
        sys.exit(1)
    return args


async def find_when_will_be_the_sun_rise(
    sun_rise_time: datetime.datetime, country: str
) -> None:
    url = "https://api.sunrisesunset.io"
    sun_rise_client = SunRiseClient(url)
    country_coordinates_client = CountryCoordinatesClient(
        "./providers/coordinates/world_cities_location.csv",
    )

    coordinates = country_coordinates_client.get(country)
    if not coordinates:
        logger.error("Country not found")
        sys.exit(1)

    day = 0
    today = datetime.date.today()
    while day != 365:
        result = await sun_rise_client.get_sunrise(
            coordinates[0],
            coordinates[1],
            str(today + datetime.timedelta(day)),
        )
        result_sun_rise_time = datetime.datetime.strptime(
            result.sun_rise_time, sun_rise_client.time_format
        )
        result_sun_rise_time = result_sun_rise_time.replace(second=0)

        if result_sun_rise_time == sun_rise_time:
            logger.info("The day is - {0}".format(result.date))
            break
        day += 1
    else:
        logger.error(
            "The day is not found - {0} time".format(
                datetime.datetime.strftime(sun_rise_time, format),
            ),
        )


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, handlers.sig_term_handler)
    signal.signal(signal.SIGABRT, handlers.sig_abort_handler)
    args = parse_args(sys.argv[1:])
    asyncio.run(
        find_when_will_be_the_sun_rise(
            args.sun_rise_time,
            args.country,
        ),
    )
