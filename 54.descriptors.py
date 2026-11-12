"""Short descriptor examples with human-like comments.

Shows a Typed data descriptor and a simple cached property.
"""

from typing import Any


class Typed:
    """Data descriptor that enforces the value type.

    We store the value in the instance.__dict__ under the provided name.
    This raises on wrong types so callers get early feedback.
    """

    def __init__(self, name: str, expected_type: type) -> None:
        self.name = name
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        # saves the attribute name if the class assigns a different one
        self.public_name = name

    def __get__(self, instance: Any, owner: type = None) -> Any:
        # when accessed on the class, return the descriptor itself
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance: Any, value: Any) -> None:
        # enforce the expected type
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} must be {self.expected_type.__name__}")
        instance.__dict__[self.name] = value


class CachedProperty:
    """A tiny cached-property: compute once, then store on the instance.

    This is a non-data descriptor (no __set__), so assigning the cached name
    on the instance bypasses future descriptor lookups.
    """

    def __init__(self, func):
        self.func = func
        self.__doc__ = getattr(func, '__doc__')

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        value = self.func(instance)
        instance.__dict__[self.func.__name__] = value
        return value


class Point:
    # descriptors: declare at the class level
    x = Typed('x', int)
    y = Typed('y', int)

    def __init__(self, x: int, y: int) -> None:
        # these assignments go through Typed.__set__
        self.x = x
        self.y = y

    @CachedProperty
    def hypot(self):
        # small computation that we'd like to cache
        print('computing hypot')
        from math import hypot
        return hypot(self.x, self.y)


if __name__ == '__main__':
    p = Point(3, 4)
    print('x, y:', p.x, p.y)

    # wrong type assignment shows the guard
    try:
        p.x = 2.5
    except TypeError as e:
        print('caught type error:', e)

    # cached property: first access computes, second returns cached value
    print('first hypot:', p.hypot)
    print('second hypot (cached):', p.hypot)
    print('instance keys:', list(p.__dict__.keys()))

'''
Q: What are descriptors in Python, and how do they work in the provided code snippet?
A: Descriptors in Python are a way to create managed attributes in classes. They are objects 
that define methods for getting, setting, and deleting an attribute's value. Descriptors work 
by implementing one or more of the following methods: `__get__`, `__set__`, and `__delete__`. When 
an attribute is accessed, assigned, or deleted, the corresponding descriptor method is called.

Q: How does the `Typed` descriptor enforce type checking in the provided code snippet?
A: The `Typed` descriptor enforces type checking by implementing the `__set__` method. When a value is 
assigned to an attribute managed by the `Typed` descriptor, the `__set__` method checks if the value 
is an instance of the expected type (specified during the descriptor's initialization). If the value 
is not of the expected type, it raises a `TypeError`, providing early feedback to the caller. This 
ensures that only values of the correct type can be assigned to the attribute.

Q: What is the purpose of the `CachedProperty` descriptor in the provided code snippet?
A: The `CachedProperty` descriptor is designed to compute a value once and then cache it for future access. 
It implements the `__get__` method, which checks if the value has already been computed and stored in the 
instance's `__dict__`. If the value has not been computed yet, it calls the associated function to compute 
the value, stores it in the instance's `__dict__`, and returns it. On subsequent accesses, it retrieves 
the cached value directly from the instance's `__dict__`, avoiding redundant computations. This is useful 
for expensive calculations that do not change over time.
'''