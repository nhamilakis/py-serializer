from typing import List, Dict

from serializer import SerializableMixin, serializable, serializer


def test_builtin_serialisation():
    # Elemental python.builtins
    assert serializer(5) == 5, "Int should not be altered"
    assert serializer(5.6) == 5.6, "Float should not be altered"
    assert serializer("I am a string") == "I am a string", "String should not be altered"
    assert serializer(None) is None, "None should remain none"


def test_list_serialisation():
    # Testing lists
    assert serializer([1, 2, 3]) == [1, 2, 3], "List of builtins should not be altered"
    assert serializer([1.4, 2.6, 3.9]) == [1.4, 2.6, 3.9], "List of builtins should not be altered"
    assert serializer(["aze", "azea", "azez"]) == ["aze", "azea", "azez"], "List of builtins should not be altered"


def test_dict_serialisation():
    # Testing dicts
    assert serializer({'x': 234, 'y': 234}) == {'x': 234, 'y': 234}, "Dict of builtins should not be altered"
    assert serializer({'x': '234', 'y': 234, 'z': 567.9}) == {'x': '234', 'y': 234, 'z': 567.9}, \
        "Dict of builtins should not be altered"


def test_rec_lists():
    x = [
        [1, 4, 5],
        {"x": 234, "name": "human"},
        "cordial",
        ["a", "b", "c"]
    ]
    assert serializer(x) == x, "Elemental List Recursion level 1 should serialize to self"

    x2 = [
        [[1, 4, 6], {"x": 4.5}, "i am not", [{"x": 1}]]
    ]

    assert serializer(x2) == x2, "Elemental List with multiple recursions should serialize to self"


def test_rec_dict():
    x = dict(
        x=[1, 2, 3, 4],
        anomaly=dict(x=1.3, y=3.4, z=6.7),
        name="not the guy"
    )
    assert serializer(x) == x, "Elemental Dict with recursion level 1 should serialize to self"

    x2 = dict(
        w=dict(w=dict(x=dict(f=[1, 4, 6]))),
        f=[1.3, 1.5, 1.6],
        name="namaste"
    )

    assert serializer(x2) == x2, "Elemental Dict with multiple recursions should serialize to self"


def test_class_mixin():
    class Test(SerializableMixin):

        def __init__(self, name: str, values: List[int]):
            self.name = name
            self.values = values

        def __serialize__(self):
            return dict(
                name=serializer(self.name),
                values=serializer(self.values)
            )

    test = Test(name="Nick", values=[1, 4, 1])
    result = dict(name="Nick", values=[1, 4, 1])
    assert serializer(test) == result, "Simple Mixin Test failed"


def test_wrapper_dataclass():
    @serializable
    class Test:
        name: str
        values: List[int]

    test = Test(name="Nick", values=[1, 4, 1])
    result = dict(name="Nick", values=[1, 4, 1])
    assert serializer(test) == result, "Simple dataclass wrapper test failed"


def test_recursive_mixin():
    class Values(SerializableMixin):

        def __init__(self, values: List[int]):
            self.values = values

        def __serialize__(self):
            return dict(
                values=serializer(self.values)
            )

    class Test(SerializableMixin):

        def __init__(self, name: str, values: Values):
            self.name = name
            self.values = values

        def __serialize__(self):
            return dict(
                name=serializer(self.name),
                values=serializer(self.values)
            )

    test = Test(name="Nick", values=Values(values=[1, 4, 1]))
    result = dict(name="Nick", values=dict(values=[1, 4, 1]))
    assert serializer(test) == result, "Recursive mixin test failed"


def test_recursive_dataclass():
    @serializable
    class Values:
        values: List[int]

    @serializable
    class Test:
        name: str
        values: Values

    test = Test(name="Nick", values=Values(values=[1, 4, 1]))
    result = dict(name="Nick", values=dict(values=[1, 4, 1]))
    assert serializer(test) == result, "Recursive dataclass test failed"


def test_recursive_dataclass2():
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

    @serializable
    class Values:
        values: List[int]

    @serializable
    class Test:
        humans: Dict[str, Person]
        values: Values

    persons = dict(
        john=Person(name="john", age=19, height=1.4, weight=14.8, address="here",
                    role=Role(role_type="manager", attributes=["lead_stuff", "decide"])),
        mark=Person(name="mark", age=19, height=1.4, weight=14.8, address="here",
                    role=Role(role_type="manager", attributes=["lead_stuff", "decide"])),
        devil=Person(name="devil", age=19, height=1.4, weight=14.8, address="here",
                     role=Role(role_type="manager", attributes=["lead_stuff", "decide"])),
    )
    test = Test(humans=persons, values=Values(values=[1, 4, 1]))
    result = dict(
        humans=dict(
            dict(
                john=dict(name="john", age=19, height=1.4, weight=14.8, address="here",
                          role=dict(role_type="manager", attributes=["lead_stuff", "decide"])),
                mark=dict(name="mark", age=19, height=1.4, weight=14.8, address="here",
                          role=dict(role_type="manager", attributes=["lead_stuff", "decide"])),
                devil=dict(name="devil", age=19, height=1.4, weight=14.8, address="here",
                           role=dict(role_type="manager", attributes=["lead_stuff", "decide"])),
            )
        ),
        values=dict(values=[1, 4, 1]))
    assert serializer(test) == result, "Complex Recursive dataclass test failed"
