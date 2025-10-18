from datetime import datetime

import pytz


class DatetimeUtils:
    @staticmethod
    def get_utc_datetime() -> datetime:
        return datetime.now(pytz.UTC).replace(tzinfo=None)
