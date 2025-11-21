"""
safe_division module: Provides safe division function with error handling
"""

def safe_division(a, b):
    """
    Safely divide two numbers, handling division by zero.
    
    Args:
        a: The numerator (dividend)
        b: The denominator (divisor)
    
    Returns:
        The result of a/b if b is not zero, otherwise returns None
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None
