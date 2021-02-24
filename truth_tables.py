""" File name:   truth_tables.py
    Author:      <your name goes here>
    Date:        <the date goes here>
    Description: This file defines a number of functions which implement Boolean
                 expressions.

                 It also defines a function to generate and print truth tables
                 using these functions.

                 It should be implemented for Exercise 2 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""
import pandas as pd
from itertools import product
def boolean_fn1(a, b, c):
    """ Return the truth value of (a ∨ b) → (-a ∧ -b) """
    return  not(a or b) or ((not a) and (not b))


def boolean_fn2(a, b, c):
    """ Return the truth value of (a ∧ b) ∨ (-a ∧ -b) """
    return (a and b) or ((not a) and (not b))


def boolean_fn3(a, b, c):
    """ Return the truth value of ((c → a) ∧ (a ∧ -b)) ∨ (-a ∧ b) """
    return ((not c or a) and (a and not b)) or (not a and b)


def draw_truth_table(boolean_fn):
    """ This function prints a truth table for the given boolean function.
        It is assumed that the supplied function has three arguments.

        ((bool, bool, bool) -> bool) -> None

        If your function is working correctly, your console output should look
        like this:

        >>> from truth_tables import *
        >>> draw_truth_table(boolean_fn1)
        a     b     c     res
        -----------------------
        False False False True
        False False True  True
        False True  False False
        False True  True  False
        True  False False False
        True  False True  False
        True  True  False False
        True  True  True  False
    """
    f = boolean_fn
    values = [list(x) + [f(*x)] for x in product([False,True], repeat=f.__code__.co_argcount)]
    return pd.DataFrame(values,columns=(list(f.__code__.co_varnames) + [f.__name__]))
