#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Adding exception handling to a function that already exists"""


def simple_lookup(var1, var2):
    """Attempts to access any index or key.

    Arguments:
        var1 (key/index): dictionary that is drawing from
        var2 (mixed): what is being lookedup in the var1

    Examples:
        >>> simple_lookup([1,2],4)
        Warning: Your index/key doesn't exist.
        [1, 2]
    """
    try:
        return var1[var2]
    except LookupError:
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
