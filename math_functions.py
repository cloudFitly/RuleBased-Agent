""" File name:   math_functions.py
    Author:      <your name goes here>
    Date:        <the date goes here>
    Description: This file defines a set of variables and simple functions.

                 It should be implemented for Exercise 1 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""
import math

ln_e = math.log(math.e , math.e)

twenty_radians =  math.radians(20)


def quotient_ceil(numerator, denominator):
    """ Returns floating_point_division numerator / denominator ...
        ... rounded up to next largest integer.
        
        (number, number) -> Integer
        
    """
    return math.ceil(numerator/denominator)
    


def quotient_floor(numerator, denominator):
    """ Returns floating_point_division numerator / denominator ...
        ... rounded down to greatest integer less then or equal to itself.
        
        (number, number, number, number) -> Integer
    """
    return math.floor(numerator/denominator)
    


def manhattan(x1, y1, x2, y2):
    """ Returns Manhattan dist. between two points (x1,y1) and (x2,y2)
        Distance Formula : |x1-x2| + |y1-y2|
        
        (number,number, number, number) -> number
    
    """
    return abs(x2-x1) + abs(y2-y1)
