#!/usr/bin/python3
"""
Write a function that prints My name is <first name> <last name>

Prototype: def say_my_name(first_name, last_name="")

You are not allowed to import any module
"""


def say_my_name(first_name, last_name=""):
    """
    first_name and last_name must be strings otherwise,

    raise a TypeError exception with the message first_name

    must be a string or last_name must be a string
    """
    try:
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        elif not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
    except TypeError:
        raise
    else:
        return print("My name is {} {}".format(first_name, last_name))


# say_my_name("Emmanuel", "Obolo")
# say_my_name("Abiodun")
# say_my_name()
# say_my_name(2, "Asaph")
# say_my_name(2, 2.25)
# say_my_name(None)
# say_my_name([2, 4, 5, 6, 8])
# say_my_name({"name": "obolo"})
# say_my_name((1, 4, 5))
# say_my_name("Asaph", 34)
