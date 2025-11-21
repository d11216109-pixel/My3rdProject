"""
Unit tests for the safe_division function
使用 Python unittest 框架測試 safe_division 函數
"""

import unittest
import sys
from io import StringIO
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """測試 safe_division 函數的各種情況"""
    
    def setUp(self):
        """在每個測試之前設置"""
        self.held_output = StringIO()
        sys.stdout = self.held_output
    
    def tearDown(self):
        """在每個測試之後清理"""
        sys.stdout = sys.__stdout__
    
    def test_normal_division(self):
        """測試正常的除法運算"""
        result = safe_division(10, 2)
        self.assertEqual(result, 5.0)
        
    def test_division_with_decimal_result(self):
        """測試產生小數結果的除法"""
        result = safe_division(7, 2)
        self.assertEqual(result, 3.5)
        
    def test_division_with_float_numbers(self):
        """測試浮點數的除法"""
        result = safe_division(10.5, 2.5)
        self.assertAlmostEqual(result, 4.2, places=1)
        
    def test_division_by_zero(self):
        """測試除以零的情況"""
        result = safe_division(10, 0)
        self.assertIsNone(result)
        output = self.held_output.getvalue()
        self.assertIn("除數不能為零", output)
        
    def test_negative_numbers(self):
        """測試負數的除法"""
        result = safe_division(-10, 2)
        self.assertEqual(result, -5.0)
        
        result = safe_division(10, -2)
        self.assertEqual(result, -5.0)
        
        result = safe_division(-10, -2)
        self.assertEqual(result, 5.0)
        
    def test_division_with_zero_numerator(self):
        """測試分子為零的情況"""
        result = safe_division(0, 10)
        self.assertEqual(result, 0.0)
        
    def test_division_with_one(self):
        """測試除以 1 的情況"""
        result = safe_division(10, 1)
        self.assertEqual(result, 10.0)
        
    def test_division_with_large_numbers(self):
        """測試大數字的除法"""
        result = safe_division(1000000, 1000)
        self.assertEqual(result, 1000.0)
        
    def test_division_with_small_numbers(self):
        """測試小數字的除法"""
        result = safe_division(0.001, 0.1)
        self.assertAlmostEqual(result, 0.01, places=2)
        
    def test_type_error_string_numerator(self):
        """測試字串作為分子時的錯誤處理"""
        result = safe_division("10", 2)
        self.assertIsNone(result)
        output = self.held_output.getvalue()
        self.assertIn("參數必須是數字", output)
        
    def test_type_error_string_denominator(self):
        """測試字串作為分母時的錯誤處理"""
        result = safe_division(10, "2")
        self.assertIsNone(result)
        output = self.held_output.getvalue()
        self.assertIn("參數必須是數字", output)
        
    def test_type_error_none_values(self):
        """測試 None 值的錯誤處理"""
        result = safe_division(None, 10)
        self.assertIsNone(result)
        
        result = safe_division(10, None)
        self.assertIsNone(result)
        
    def test_division_fractional_result(self):
        """測試產生分數結果的除法"""
        result = safe_division(1, 3)
        self.assertAlmostEqual(result, 0.3333333333333333, places=10)


class TestSafeDivisionEdgeCases(unittest.TestCase):
    """測試 safe_division 的邊界情況"""
    
    def setUp(self):
        """在每個測試之前設置"""
        self.held_output = StringIO()
        sys.stdout = self.held_output
    
    def tearDown(self):
        """在每個測試之後清理"""
        sys.stdout = sys.__stdout__
    
    def test_very_large_division(self):
        """測試非常大的數字除法"""
        result = safe_division(10**100, 10**50)
        self.assertAlmostEqual(result, 10**50, places=-40)
        
    def test_very_small_division(self):
        """測試非常小的數字除法"""
        result = safe_division(10**-10, 10**-5)
        self.assertAlmostEqual(result, 10**-5, places=15)
        
    def test_boolean_values(self):
        """測試布林值（在 Python 中可以作為數字使用）"""
        result = safe_division(True, True)
        self.assertEqual(result, 1.0)
        
        result = safe_division(10, True)
        self.assertEqual(result, 10.0)


if __name__ == '__main__':
    # 執行所有測試
    unittest.main(verbosity=2)
