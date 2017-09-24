"""
Calculates the expression.
Parses an expression and evaluates using eval function.
"""
import parser
from math import log

def evaluator(expression):
    """
    Parses an expression and evaluates using eval function.
    """
    parsed = parser.expr(expression)
    return eval(parsed.compile())
