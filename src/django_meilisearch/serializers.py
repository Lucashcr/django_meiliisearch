from datetime import datetime

from django.utils.timezone import get_current_timezone
from rest_framework import serializers


class TimestampField(serializers.DateTimeField):
    """
    Convert a django datetime to/from timestamp.
    """
    def to_representation(self, value):
        """
        Convert the field to its internal representation (aka timestamp)
        :param value: the DateTime value
        :return: a UTC timestamp integer
        """
        return value.timestamp()

    def to_internal_value(self, value):
        """
        deserialize a timestamp to a DateTime value
        :param value: the timestamp value
        :return: a django DateTime value
        """
        tz = get_current_timezone()
        return datetime.fromtimestamp(value, tz)