# 單元測試結果報告

## 測試執行說明

本報告記錄了 `safe_division` 函式的單元測試結果，包含綠燈（通過）和紅燈（失敗）的情況。

---

## 綠燈（通過）- 完整版本測試結果

### 測試執行命令
```bash
python3 -m unittest test_safe_division.py -v
```

### 測試結果
```
test_boundary_values (test_safe_division.TestSafeDivision.test_boundary_values)
測試邊界值相除 ... ok
test_division_by_zero (test_safe_division.TestSafeDivision.test_division_by_zero)
測試除以零的情況 - 應該回傳 None 而不是拋出錯誤 ... ok
test_negative_division (test_safe_division.TestSafeDivision.test_negative_division)
測試負數相除 ... ok
test_normal_division (test_safe_division.TestSafeDivision.test_normal_division)
測試正常的數值相除 ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

### 綠燈測試案例說明

1. **test_normal_division (正常的數值相除)** ✅
   - 測試 10 ÷ 2 = 5.0
   - 測試 20 ÷ 4 = 5.0
   - 測試 100 ÷ 10 = 10.0
   - **結果：通過**

2. **test_negative_division (負數相除)** ✅
   - 測試 -10 ÷ 2 = -5.0
   - 測試 10 ÷ -2 = -5.0
   - 測試 -10 ÷ -2 = 5.0
   - **結果：通過**

3. **test_boundary_values (邊界值相除)** ✅
   - 測試 1 ÷ 1 = 1.0
   - 測試 0 ÷ 5 = 0.0
   - 測試 1 ÷ 3 ≈ 0.333...
   - **結果：通過**

4. **test_division_by_zero (除以零的情況)** ✅
   - 測試 10 ÷ 0 應該回傳 None
   - 測試 0 ÷ 0 應該回傳 None
   - 測試 -10 ÷ 0 應該回傳 None
   - **結果：通過**

**結論：** 所有測試都通過，顯示為綠燈。這代表 `safe_division` 函式能正確處理各種情境，包含處理除以零的狀況，使程式不會當機。

---

## 紅燈（失敗）- 移除除以零處理後的測試結果

### 測試執行說明
當我將 `safe_division` 函式中的「處理除以零」的程式碼註解或刪除後（參考 `safe_division_broken.py`），再次執行單元測試。

### 移除的程式碼
```python
# 原始版本（有防呆機制）
def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# 移除防呆機制後的版本
def safe_division(a, b):
    return a / b
```

### 測試執行命令
```bash
python3 -m unittest test_safe_division_broken.py -v
```

### 測試結果
```
test_boundary_values (test_safe_division_broken.TestSafeDivision.test_boundary_values)
測試邊界值相除 ... ok
test_division_by_zero (test_safe_division_broken.TestSafeDivision.test_division_by_zero)
測試除以零的情況 - 應該回傳 None 而不是拋出錯誤 ... ERROR
test_negative_division (test_safe_division_broken.TestSafeDivision.test_negative_division)
測試負數相除 ... ok
test_normal_division (test_safe_division_broken.TestSafeDivision.test_normal_division)
測試正常的數值相除 ... ok

======================================================================
ERROR: test_division_by_zero (test_safe_division_broken.TestSafeDivision.test_division_by_zero)
測試除以零的情況 - 應該回傳 None 而不是拋出錯誤
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_safe_division_broken.py", line 32, in test_division_by_zero
    result = safe_division(10, 0)
  File "safe_division_broken.py", line 26, in safe_division
    return a / b
ZeroDivisionError: division by zero

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (errors=1)
```

---

## 哪個測試失敗？請簡單說明原因

### 失敗的測試
**test_division_by_zero (測試除以零的情況)**

### 失敗原因
失敗的是測試「當 b 為零時，safe_division 是否能妥善處理」的單元測試。原因是函式內部沒有處理除以零的例外，導致執行時拋出 `ZeroDivisionError` 錯誤，測試無法通過。

### 詳細說明
1. **預期行為**：當除數為零時，函式應該回傳 `None`，而不是拋出錯誤
2. **實際行為**：由於移除了 `try-except` 區塊，當執行 `return a / b` 且 `b` 為 0 時，Python 直接拋出 `ZeroDivisionError`
3. **測試失敗點**：在執行 `result = safe_division(10, 0)` 這一行時，程式就直接崩潰了，無法繼續執行後續的斷言檢查

### 重要性
這也證明了防呆機制的重要性，能讓程式更加穩定安全。透過適當的例外處理：
- ✅ 程式不會因為除以零而崩潰
- ✅ 可以優雅地處理錯誤情況
- ✅ 提供更好的使用者體驗
- ✅ 讓程式更加健壯（robust）

---

## 檔案說明

### 主要檔案
1. **safe_division.py** - 完整版本的 safe_division 函式（包含除以零處理）
2. **test_safe_division.py** - 完整版本的單元測試
3. **safe_division_broken.py** - 移除除以零處理的版本（用於示範失敗情況）
4. **test_safe_division_broken.py** - 對應 broken 版本的單元測試

### 執行測試的方法

#### 執行成功的測試（綠燈）
```bash
python3 -m unittest test_safe_division.py -v
```

#### 執行失敗的測試（紅燈）
```bash
python3 -m unittest test_safe_division_broken.py -v
```
