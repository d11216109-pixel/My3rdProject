"""
safe_division module: Broken version WITHOUT division by zero handling
This version is used to demonstrate test failures (red lights)
"""

def safe_division(a, b):
    """
    **此版本已故意移除除以零的處理，用於演示測試失敗（紅燈）**
    
    注意：此版本已將除以零的處理程式碼註解掉，用於演示測試失敗
    
    Args:
        a: The numerator (dividend)
        b: The denominator (divisor)
    
    Returns:
        The result of a/b
        警告：當 b 為 0 時會拋出 ZeroDivisionError（這是故意的，用於演示）
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)  # 會拋出 ZeroDivisionError
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero
    """
    # try:
    return a / b
    # except ZeroDivisionError:
    #     return None
