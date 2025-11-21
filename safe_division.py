"""
safe_division module - Provides a safe division function with error handling
"""


def safe_division(numerator, denominator):
    """
    Safely divides two numbers with error handling for division by zero.
    
    Args:
        numerator: The number to be divided (dividend)
        denominator: The number to divide by (divisor)
    
    Returns:
        The result of numerator / denominator if successful
        None if denominator is zero or if an error occurs
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
        >>> safe_division(7, 2)
        3.5
    """
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("錯誤：除數不能為零")
        return None
    except TypeError:
        print("錯誤：參數必須是數字")
        return None
    except Exception as e:
        print(f"發生未預期的錯誤：{e}")
        return None
