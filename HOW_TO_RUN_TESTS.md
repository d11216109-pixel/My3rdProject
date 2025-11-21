# 如何執行測試

## 快速開始

本專案包含 `safe_division` 函式的單元測試範例，用於展示綠燈（通過）與紅燈（失敗）的測試結果。

## 執行測試

### 1. 執行正常版本的測試（預期全部通過 ✅）

```bash
python3 -m unittest test_safe_division.py -v
```

**預期結果：** 所有 4 個測試都通過（綠燈）

### 2. 執行移除防呆機制的版本（預期會失敗 ❌）

```bash
python3 -m unittest test_safe_division_broken.py -v
```

**預期結果：** `test_division_by_zero` 測試會失敗（紅燈），拋出 `ZeroDivisionError`

### 3. 執行兩個版本的對比測試

```bash
echo "=== 正常版本（有防呆機制）===" && \
python3 -m unittest test_safe_division.py && \
echo -e "\n=== 移除防呆機制版本 ===" && \
python3 -m unittest test_safe_division_broken.py || true
```

## 檔案說明

| 檔案名稱 | 說明 |
|---------|------|
| `safe_division.py` | 包含除以零處理的正常版本 |
| `test_safe_division.py` | 正常版本的單元測試 |
| `safe_division_broken.py` | 移除除以零處理的版本（用於演示失敗） |
| `test_safe_division_broken.py` | broken 版本的單元測試 |
| `TEST_RESULTS.md` | 詳細的測試結果報告 |

## 測試案例

每個測試檔案都包含 4 個測試案例：

1. **test_normal_division** - 測試正常的數值相除
2. **test_negative_division** - 測試負數相除
3. **test_boundary_values** - 測試邊界值相除
4. **test_division_by_zero** - 測試除以零的情況

## 學習重點

透過比較兩個版本的測試結果，可以學習到：

1. ✅ 防呆機制（try-except）的重要性
2. ✅ 單元測試如何幫助發現程式問題
3. ✅ 綠燈（通過）和紅燈（失敗）的差異
4. ✅ 例外處理讓程式更加穩定安全

## 詳細報告

完整的測試結果分析請參考 [TEST_RESULTS.md](TEST_RESULTS.md)
