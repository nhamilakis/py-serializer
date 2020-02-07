#  The MIT License (MIT)
#
#  Copyright (c) 2020 Nicolas Hamilakis
#

from dataclasses import Field


class NotSerializableInstance(Exception):
    pass


# todo maybe more complex conversion can be achieved when using Field typing
def serializer(value: object, name: str = None, field: Field = None):
    """ Serialize an object """
    base_types = [str, int, float, bool]

    # Base type no conversion
    if type(value) in base_types:
        return value

    # Special cases
    # TODO ?? complex ??

    if type(value) is list:
        return [
            serializer(v) for v in value
        ]

    if type(value) is dict:
        return {
            x: serializer(y) for x, y in value.items()
        }

    if type(value) is tuple:
        return (
            serializer(x) for x in value
        )

    # Generic serializable obj
    if hasattr(value, "__serialize__"):
        return value.__serialize__()

    # None is allowed
    if value is None:
        return None

    name = value.__name__ if hasattr(value, '__name__') else ""
    raise NotSerializableInstance(f"Object({name}, {type(value)}) could not be serialized !!")
