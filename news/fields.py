try:
    import pytz
except ImportError:
    raise ImportError('You need to install the "pytz" module first.')

import datetime
import time

from django.conf import settings
from django.core import exceptions
from django.db.models import DateTimeField as DjangoDateTimeField
from django.utils.encoding import smart_str
from django.utils.translation import ugettext as _

localtz = pytz.timezone(settings.TIME_ZONE)


class DateTimeField(DjangoDateTimeField):
    """
    Same as Django's DateTimeField, but this one understands 'YYYY-MM-DD HH:MM[:ss[.uuuuuu]]Z format
    (notice the Z at the end, which means the datetime is specified in UTC), which will be converted into
    the local server timezone (based on the TIME_ZONE setting).
    """
    def to_python(self, value):
        if value is None:
            return value
        if isinstance(value, datetime.datetime):
            return value
        if isinstance(value, datetime.date):
            return datetime.datetime(value.year, value.month, value.day)

        # Attempt to parse a datetime:
        value = smart_str(value)
        # split usecs, because they are not recognized by strptime.
        if '.' in value:
            try:
                value, usecs = value.split('.')
                usecs = int(usecs)
            except ValueError:
                raise exceptions.ValidationError(
                    _('Enter a valid date/time in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][Z] format.'))
        else:
            usecs = 0
        kwargs = {'microsecond': usecs}
        try:  # Seconds are optional, so try converting seconds first.
            if value.endswith('Z'):
                value = value.strip('Z')
                retval = pytz.utc.localize(datetime.datetime(*time.strptime(value, '%Y-%m-%d %H:%M:%S')[:6],
                                           **kwargs))
                return retval.astimezone(localtz)
            else:
                return datetime.datetime(*time.strptime(value, '%Y-%m-%d %H:%M:%S')[:6],
                                         **kwargs)

        except ValueError as e:
            try:  # Try without seconds.
                if value.endswith('Z'):
                    value = value.strip('Z')
                    retval = pytz.utc.localize(datetime.datetime(*time.strptime(value, '%Y-%m-%d %H:%M')[:5],
                                                                 **kwargs))
                    return retval.astimezone(localtz)
                else:
                    return datetime.datetime(*time.strptime(value, '%Y-%m-%d %H:%M')[:5],
                                             **kwargs)
            except ValueError as e:  # Try without hour/minutes/seconds.
                try:
                    if value.endswith('Z'):
                        value = value.strip('Z')
                        retval = pytz.utc.localize(datetime.datetime(*time.strptime(value, '%Y-%m-%d')[:3],
                                                   **kwargs))
                        return retval.astimezone(localtz)
                    else:
                        return datetime.datetime(*time.strptime(value, '%Y-%m-%d')[:3],
                                                 **kwargs)
                except ValueError as e:
                    raise exceptions.ValidationError(
                        _('Enter a valid date/time in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][Z] format.'))


