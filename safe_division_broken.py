"""
safe_division module: Broken version WITHOUT division by zero handling
This version is used to demonstrate test failures (red lights)
"""

def safe_division(a, b):
    """
    Safely divide two numbers, handling division by zero.
    
    注意：此版本已將除以零的處理程式碼註解掉，用於演示測試失敗
    
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
    # try:
    return a / b
    # except ZeroDivisionError:
    #     return None
