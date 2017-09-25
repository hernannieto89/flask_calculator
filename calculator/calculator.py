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
    # This version is very prone to security issues.
    # In the future a restricted version of eval should be used.
    parsed = parser.expr(expression)
    return eval(parsed.compile())
