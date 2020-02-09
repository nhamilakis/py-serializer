## Serializer

A serialization module for python objects

![Test](https://github.com/nhamilakis/py-serializer/workflows/Test/badge.svg) ![Upload Python Package](https://github.com/nhamilakis/py-serializer/workflows/Upload%20Python%20Package/badge.svg) [![PyPI version](https://badge.fury.io/py/py-serializer.svg)](https://badge.fury.io/py/py-serializer) 

## Quickstart

> `pip install py-serializer`


```python
from typing import List
from serializer import serializable

@serializable
class Role:
    role_type: str
    attributes: List[str]

@serializable
class Person:
    name: str
    age: int
    height: float
    weight: float
    address: str
    role: List[Role]


p = Person(
    name="Paul", age=25, height=1.70, weight=83.5, address="earth",
    role=[Role(role_type='human', attributes=['speak', 'eat', 'sleep'])]
)

print(p.to_dict())
```

> ```
> {
>     'name': 'Paul', 
>     'age': 25, 
>     'height': 1.7,
>     'weight': 83.5, 
>     'address': 'earth', 
>     'role': [
>           {
>             'role_type': 'human',
>             'attributes': ['speak', 'eat', 'sleep']
>           }
>     ]
> }
>```


**Serializable wrapper extends *dataclass* so you can treat it like a normal dataclass.**


## Mixin

It is possible to have a class extend abstract class SerializableMixin

```python
from serializer import SerializableMixin, serializer

class Test(SerializableMixin):
    
    def __init__(self, name: str):
        self.name = name

    def __serialize__(self):
        return dict(name=serializer(self.name))
```

> `>> Test(name='Paul').to_dict()`

> `{ 'name': 'Paul' } `

For object to be seriazable they only need to implement a `__serialize__` method.