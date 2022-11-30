import re
from src.main.time.dates.formats import validation
from src.main.time.dates.formats.interface import DateFormatter
from src.main.time.months import factory as months_factory
from src.main.time.years import factory as years_factory


class NumericFormatter(DateFormatter):
    def __init__(self, date: str):
        validation.assert_numeric_format_is_valid(date)
        self._date = date

    @property
    def day(self) -> int:
        return int(self._date[0:2])

    @property
    def month(self) -> int:
        return int(self._date[2:4])

    @property
    def year(self) -> int:
        return years_factory.full_year(self._date[4:])


class NumericDelimitedFormatter(DateFormatter):
    def __init__(self, date: str):
        split_parts = re.split(r"\W+", date)
        self._parts = list(map(
            int, filter(lambda date_part: bool(date_part), split_parts)))

    @property
    def day(self) -> int:
        return self._parts[0]

    @property
    def month(self) -> int:
        return self._parts[1]

    @property
    def year(self) -> int:
        return years_factory.full_year(self._parts[2])


class AlphanumericFormatter(DateFormatter):
    def __init__(self, date: str):
        split_parts = re.split(r"\W+", date)
        cleaned_parts = list(filter(lambda d: bool(d), split_parts))

        self._parts = [
            int(cleaned_parts[0]),
            months_factory.month_no(cleaned_parts[1]),
            years_factory.full_year(cleaned_parts[2])
        ]

    @property
    def day(self) -> int:
        return self._parts[0]

    @property
    def month(self) -> int:
        return self._parts[1]

    @property
    def year(self) -> int:
        return self._parts[2]
