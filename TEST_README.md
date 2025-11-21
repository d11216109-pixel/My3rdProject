# safe_division 單元測試說明

## 專案描述

本專案包含 `safe_division` 函數及其完整的單元測試。`safe_division` 是一個安全的除法函數，能夠處理各種邊界情況和錯誤。

## 檔案說明

- **safe_division.py**: 包含 `safe_division` 函數的主要實作
- **test_safe_division.py**: 包含完整的單元測試

## safe_division 函數功能

`safe_division(numerator, denominator)` 函數提供以下功能：

1. **正常除法運算**: 對兩個數字進行除法運算
2. **除以零保護**: 當除數為零時，返回 None 並顯示錯誤訊息
3. **類型錯誤處理**: 當參數不是數字時，返回 None 並顯示錯誤訊息
4. **異常處理**: 捕捉並處理所有未預期的錯誤

## 測試涵蓋範圍

單元測試涵蓋以下情況：

### 基本功能測試 (TestSafeDivision)
1. ✅ 正常的除法運算 (10 / 2 = 5.0)
2. ✅ 產生小數結果的除法 (7 / 2 = 3.5)
3. ✅ 浮點數的除法 (10.5 / 2.5 = 4.2)
4. ✅ 除以零的情況 (10 / 0 = None)
5. ✅ 負數的除法
   - 負數 ÷ 正數
   - 正數 ÷ 負數
   - 負數 ÷ 負數
6. ✅ 分子為零的情況 (0 / 10 = 0.0)
7. ✅ 除以 1 的情況 (10 / 1 = 10.0)
8. ✅ 大數字的除法 (1,000,000 / 1,000 = 1,000.0)
9. ✅ 小數字的除法 (0.001 / 0.1 = 0.01)
10. ✅ 字串作為分子時的錯誤處理
11. ✅ 字串作為分母時的錯誤處理
12. ✅ None 值的錯誤處理
13. ✅ 產生分數結果的除法 (1 / 3 = 0.333...)

### 邊界情況測試 (TestSafeDivisionEdgeCases)
1. ✅ 非常大的數字除法 (10^100 / 10^50)
2. ✅ 非常小的數字除法 (10^-10 / 10^-5)
3. ✅ 布林值作為參數 (True / True = 1.0)

## 如何執行測試

### 執行所有測試
```bash
python test_safe_division.py
```

### 使用 unittest 執行測試
```bash
python -m unittest test_safe_division.py
```

### 執行測試並顯示詳細資訊
```bash
python test_safe_division.py -v
```

## 測試結果

所有 16 個測試案例均通過：

```
----------------------------------------------------------------------
Ran 16 tests in 0.001s

OK
```

## 測試統計

- **總測試數**: 16
- **測試類別數**: 2
- **通過率**: 100%
- **涵蓋情境**:
  - 正常運算: 9 個測試
  - 錯誤處理: 4 個測試
  - 邊界情況: 3 個測試

## 使用範例

```python
from safe_division import safe_division

# 正常使用
result = safe_division(10, 2)
print(result)  # 輸出: 5.0

# 除以零
result = safe_division(10, 0)
print(result)  # 輸出: None，並顯示錯誤訊息

# 小數除法
result = safe_division(7, 2)
print(result)  # 輸出: 3.5

# 錯誤輸入
result = safe_division("10", 2)
print(result)  # 輸出: None，並顯示錯誤訊息
```

## 技術細節

- **測試框架**: Python unittest
- **Python 版本**: Python 3.x
- **測試方法**: 
  - assertEqual: 驗證精確相等
  - assertAlmostEqual: 驗證浮點數近似相等
  - assertIsNone: 驗證返回 None
  - assertIn: 驗證錯誤訊息

## 作者

使用 GitHub Copilot 自動生成
