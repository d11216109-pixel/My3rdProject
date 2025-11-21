"""
Unit tests for safe_division function
"""
import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for the safe_division function"""
    
    def test_normal_division(self):
        """測試正常的數值相除"""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(20, 4), 5.0)
        self.assertEqual(safe_division(100, 10), 10.0)
    
    def test_negative_division(self):
        """測試負數相除"""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_boundary_values(self):
        """測試邊界值相除"""
        self.assertEqual(safe_division(1, 1), 1.0)
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertAlmostEqual(safe_division(1, 3), 0.3333333333333333)
    
    def test_division_by_zero(self):
        """測試除以零的情況 - 應該回傳 None 而不是拋出錯誤"""
        result = safe_division(10, 0)
        self.assertIsNone(result)
        
        result = safe_division(0, 0)
        self.assertIsNone(result)
        
        result = safe_division(-10, 0)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
