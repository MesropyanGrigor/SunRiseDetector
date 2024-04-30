import csv


class CountryCoordinatesClient(object):
    def __init__(self, file_name: str = "world_cities_location.csv"):
        self._city_coordinates = {}
        with open(file_name) as csv_file:
            city_reader = csv.reader(csv_file, delimiter=";")
            self._city_coordinates = {
                row[2].lower(): (row[3], row[4]) for row in city_reader
            }

    def get(self, city_name: str) -> tuple[str, str] | None:
        coordinates = self._city_coordinates.get(city_name.lower())
        return coordinates


# country_coordinates = CountryCoordinates()

# print(country_coordinates.get("paris"))
