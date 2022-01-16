from .models import STATUS

mapping = dict(STATUS.choices())


def status_from_int_to_str(val):
    return mapping[val]

