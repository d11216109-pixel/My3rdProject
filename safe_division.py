# 防呆 safe_division 函式
def safe_division(a, b):
    """
    安全的除法函式，能防止除以零的錯誤
    
    參數:
        a: 被除數
        b: 除數
    
    回傳值:
        如果 b 不為零，回傳 a / b 的結果
        如果 b 為零，回傳 None 並印出錯誤訊息
    """
    if b == 0:
        print("錯誤：除數不能為零！")
        return None
    return a / b


# 測試範例
if __name__ == "__main__":
    print("=== safe_division 函式測試 ===")
    
    # 測試正常除法
    result1 = safe_division(10, 2)
    print(f"10 / 2 = {result1}")
    
    # 測試小數除法
    result2 = safe_division(7, 3)
    print(f"7 / 3 = {result2}")
    
    # 測試除以零
    result3 = safe_division(10, 0)
    print(f"10 / 0 = {result3}")
    
    # 測試負數除法
    result4 = safe_division(-10, 2)
    print(f"-10 / 2 = {result4}")
    
    # 測試浮點數除法
    result5 = safe_division(5.5, 2.5)
    print(f"5.5 / 2.5 = {result5}")
