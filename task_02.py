#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Error for a invalid age"""
    pass


def get_age(birthyear):
    """Converting birth year to age.

    Arguments:
        birthyear (int): year a person was born.

    Returns:
        int: a persons age

    Examples:
        >>> get_age(2000)
        15

    Raises:
        InvalidAgeError: This is an invalid birthyear.
    """
    age = datetime.datetime.now().year - birthyear
    if age > 0:
        return age
    else:
        raise InvalidAgeError('This is an invalid birthyear.')
