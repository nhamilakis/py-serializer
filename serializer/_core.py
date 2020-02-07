#  The MIT License (MIT)
#
#  Copyright (c) 2020 Nicolas Hamilakis
#

import abc
from dataclasses import dataclass

from ._serializer import NotSerializableInstance, serializer


class NotADataClassInstance(Exception):
    """ Raised when trying to serialize a class without the __dataclass_fields__ attribute """
    pass


class _Serializable(abc.ABC):

    def to_dict(self):
        """ Class function allowing conversion of an object to a dictionary"""
        if hasattr(self, '__serialize__'):
            return self.__serialize__()
        raise NotSerializableInstance(f"Could not serialize  {type(self)} object.")

    @abc.abstractmethod
    def __serialize__(self):
        raise NotImplemented("abstract method")


class _SerializableDataclassMixin(_Serializable):
    """ A mixin class to add serializer functions to dataclasses """

    def __serialize__(self):
        if hasattr(self, '__dataclass_fields__'):
            result = {}
            for name, field in self.__dataclass_fields__.items():
                result[name] = serializer(getattr(self, name), name, field)
            return result
        raise NotADataClassInstance(f"Could not infer dataclass fields from {type(self)} object.")

    @classmethod
    def mixin(cls, klass, *args, **kwargs):
        """ Attach methods to klass """
        setattr(klass, 'to_dict', cls.to_dict)
        setattr(klass, '__serialize__', cls.__serialize__)
        return dataclass(klass, *args, **kwargs)


def serializable(_cls=None, *args, **kwargs):
    """ Wrapper to transform class into serializable (Note: extends dataclass) """

    def wrap(cls):
        return _SerializableDataclassMixin.mixin(klass=cls, *args, **kwargs)

    if _cls is None:
        return wrap
    return wrap(_cls)
