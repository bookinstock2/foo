"""科学计算器测试模块"""

import pytest
import math
from calculator import ScientificCalculator


class TestAdd:
    """加法运算的测试类"""

    def test_add_positive_numbers(self):
        """测试正数加法"""
        assert ScientificCalculator.add(2, 3) == 5

    def test_add_negative_numbers(self):
        """测试负数加法"""
        assert ScientificCalculator.add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        """测试正负数混合加法"""
        assert ScientificCalculator.add(-2, 5) == 3

    def test_add_zero(self):
        """测试与零相加"""
        assert ScientificCalculator.add(0, 5) == 5
        assert ScientificCalculator.add(5, 0) == 5
        assert ScientificCalculator.add(0, 0) == 0

    def test_add_floats(self):
        """测试浮点数加法"""
        assert ScientificCalculator.add(1.5, 2.5) == 4.0

    def test_add_large_numbers(self):
        """测试大数字加法"""
        assert ScientificCalculator.add(1000000, 2000000) == 3000000


class TestSubtract:
    """减法运算的测试类"""

    def test_subtract_positive_numbers(self):
        """测试正数减法"""
        assert ScientificCalculator.subtract(5, 3) == 2

    def test_subtract_negative_numbers(self):
        """测试负数减法"""
        assert ScientificCalculator.subtract(-5, -3) == -2

    def test_subtract_mixed_numbers(self):
        """测试正负数混合减法"""
        assert ScientificCalculator.subtract(5, -3) == 8
        assert ScientificCalculator.subtract(-5, 3) == -8

    def test_subtract_zero(self):
        """测试减零"""
        assert ScientificCalculator.subtract(5, 0) == 5

    def test_subtract_same_number(self):
        """测试相同数字相减"""
        assert ScientificCalculator.subtract(5, 5) == 0

    def test_subtract_floats(self):
        """测试浮点数减法"""
        assert ScientificCalculator.subtract(5.5, 2.5) == 3.0


class TestMultiply:
    """乘法运算的测试类"""

    def test_multiply_positive_numbers(self):
        """测试正数乘法"""
        assert ScientificCalculator.multiply(3, 4) == 12

    def test_multiply_negative_numbers(self):
        """测试负数乘法（两个负数相乘）"""
        assert ScientificCalculator.multiply(-3, -4) == 12

    def test_multiply_mixed_sign(self):
        """测试正负数乘法"""
        assert ScientificCalculator.multiply(-3, 4) == -12
        assert ScientificCalculator.multiply(3, -4) == -12

    def test_multiply_by_zero(self):
        """测试乘以零"""
        assert ScientificCalculator.multiply(5, 0) == 0
        assert ScientificCalculator.multiply(0, 5) == 0
        assert ScientificCalculator.multiply(0, 0) == 0

    def test_multiply_by_one(self):
        """测试乘以1"""
        assert ScientificCalculator.multiply(5, 1) == 5
        assert ScientificCalculator.multiply(1, 5) == 5

    def test_multiply_floats(self):
        """测试浮点数乘法"""
        assert ScientificCalculator.multiply(2.5, 4.0) == 10.0

    def test_multiply_large_numbers(self):
        """测试大数字乘法"""
        assert ScientificCalculator.multiply(1000, 2000) == 2000000


class TestDivide:
    """除法运算的测试类"""

    def test_divide_positive_numbers(self):
        """测试正数除法"""
        assert ScientificCalculator.divide(10, 2) == 5

    def test_divide_negative_numbers(self):
        """测试负数除法"""
        assert ScientificCalculator.divide(-10, -2) == 5

    def test_divide_mixed_sign(self):
        """测试正负数除法"""
        assert ScientificCalculator.divide(-10, 2) == -5
        assert ScientificCalculator.divide(10, -2) == -5

    def test_divide_floats(self):
        """测试浮点数除法"""
        assert ScientificCalculator.divide(10.0, 2.0) == 5.0
        assert abs(ScientificCalculator.divide(10, 3) - 3.333333333333) < 1e-9, \
            "除法结果应接近 3.333333"

    def test_divide_by_zero_raises_error(self):
        """测试除以零抛出异常"""
        with pytest.raises(ValueError, match="除数不能为零"):
            ScientificCalculator.divide(10, 0)

    def test_divide_zero_by_number(self):
        """测试零除以非零数"""
        assert ScientificCalculator.divide(0, 5) == 0

    def test_divide_invalid_type_raises_error(self):
        """测试非数字类型抛出异常"""
        with pytest.raises(TypeError, match="参数必须是数字类型"):
            ScientificCalculator.divide("10", 2)
        with pytest.raises(TypeError, match="参数必须是数字类型"):
            ScientificCalculator.divide(10, "2")

    def test_divide_result_precision(self):
        """测试除法精度"""
        result = ScientificCalculator.divide(1, 3)
        assert abs(result - 0.333333333333) < 1e-9


class TestPower:
    """幂运算的测试类"""

    def test_power_positive_exponent(self):
        """测试正指数"""
        assert ScientificCalculator.power(2, 3) == 8
        assert ScientificCalculator.power(5, 2) == 25

    def test_power_zero_exponent(self):
        """测试零指数"""
        assert ScientificCalculator.power(5, 0) == 1
        assert ScientificCalculator.power(0, 0) == 1
        assert ScientificCalculator.power(-5, 0) == 1

    def test_power_negative_exponent(self):
        """测试负指数"""
        assert ScientificCalculator.power(2, -1) == 0.5
        assert abs(ScientificCalculator.power(2, -2) - 0.25) < 1e-9
        assert abs(ScientificCalculator.power(10, -1) - 0.1) < 1e-9

    def test_power_negative_base(self):
        """测试负底数"""
        assert ScientificCalculator.power(-2, 2) == 4
        assert ScientificCalculator.power(-2, 3) == -8
        assert ScientificCalculator.power(-5, 0) == 1

    def test_power_float_base(self):
        """测试浮点数底数"""
        assert abs(ScientificCalculator.power(2.5, 2) - 6.25) < 1e-9

    def test_power_float_exponent(self):
        """测试浮点数指数"""
        assert abs(ScientificCalculator.power(4, 0.5) - 2.0) < 1e-9
        assert abs(ScientificCalculator.power(8, 1/3) - 2.0) < 1e-9

    def test_power_base_zero(self):
        """测试底数为零"""
        assert ScientificCalculator.power(0, 1) == 0
        assert ScientificCalculator.power(0, 5) == 0

    def test_power_invalid_type_raises_error(self):
        """测试非数字类型抛出异常"""
        with pytest.raises(TypeError, match="参数必须是数字类型"):
            ScientificCalculator.power("2", 3)
        with pytest.raises(TypeError, match="参数必须是数字类型"):
            ScientificCalculator.power(2, "3")

    def test_power_large_numbers(self):
        """测试大数字幂运算"""
        assert ScientificCalculator.power(10, 6) == 1000000


class TestSqrt:
    """平方根运算的测试类"""

    def test_sqrt_perfect_square(self):
        """测试完全平方数"""
        assert ScientificCalculator.sqrt(4) == 2
        assert ScientificCalculator.sqrt(9) == 3
        assert ScientificCalculator.sqrt(16) == 4
        assert ScientificCalculator.sqrt(100) == 10

    def test_sqrt_zero(self):
        """测试零的平方根"""
        assert ScientificCalculator.sqrt(0) == 0

    def test_sqrt_one(self):
        """测试1的平方根"""
        assert ScientificCalculator.sqrt(1) == 1

    def test_sqrt_non_perfect_square(self):
        """测试非完全平方数"""
        assert abs(ScientificCalculator.sqrt(2) - math.sqrt(2)) < 1e-9
        assert abs(ScientificCalculator.sqrt(5) - math.sqrt(5)) < 1e-9
        assert abs(ScientificCalculator.sqrt(10) - math.sqrt(10)) < 1e-9

    def test_sqrt_float_number(self):
        """测试浮点数的平方根"""
        assert abs(ScientificCalculator.sqrt(2.25) - 1.5) < 1e-9
        assert abs(ScientificCalculator.sqrt(0.25) - 0.5) < 1e-9

    def test_sqrt_large_number(self):
        """测试大数字的平方根"""
        assert ScientificCalculator.sqrt(1000000) == 1000

    def test_sqrt_negative_number_raises_error(self):
        """测试负数抛出异常"""
        with pytest.raises(ValueError, match="不能对负数进行平方根运算"):
            ScientificCalculator.sqrt(-1)
        with pytest.raises(ValueError, match="不能对负数进行平方根运算"):
            ScientificCalculator.sqrt(-10)

    def test_sqrt_invalid_type_raises_error(self):
        """测试非数字类型抛出异常"""
        with pytest.raises(TypeError, match="参数必须是数字类型"):
            ScientificCalculator.sqrt("4")
        with pytest.raises(TypeError, match="参数必须是数字类型"):
            ScientificCalculator.sqrt([4])


class TestLog:
    """对数运算的测试类"""

    def test_log_base_10_standard(self):
        """测试以10为底的对数（标准对数）"""
        assert abs(ScientificCalculator.log(1) - 0.0) < 1e-9
        assert abs(ScientificCalculator.log(10) - 1.0) < 1e-9
        assert abs(ScientificCalculator.log(100) - 2.0) < 1e-9
        assert abs(ScientificCalculator.log(1000) - 3.0) < 1e-9

    def test_log_base_e_natural_log(self):
        """测试以e为底的对数（自然对数）"""
        assert abs(ScientificCalculator.log(1, math.e) - 0.0) < 1e-9
        assert abs(ScientificCalculator.log(math.e, math.e) - 1.0) < 1e-9

    def test_log_base_2_binary_log(self):
        """测试以2为底的对数"""
        assert abs(ScientificCalculator.log(1, 2) - 0.0) < 1e-9
        assert abs(ScientificCalculator.log(2, 2) - 1.0) < 1e-9
        assert abs(ScientificCalculator.log(4, 2) - 2.0) < 1e-9
        assert abs(ScientificCalculator.log(8, 2) - 3.0) < 1e-9

    def test_log_fraction_values(self):
        """测试分数对数值"""
        assert abs(ScientificCalculator.log(0.1, 10) - (-1.0)) < 1e-9
        assert abs(ScientificCalculator.log(0.01, 10) - (-2.0)) < 1e-9

    def test_log_zero_true_number_raises_error(self):
        """测试真数为零抛出异常"""
        with pytest.raises(ValueError, match="对数的真数必须大于0"):
            ScientificCalculator.log(0, 10)

    def test_log_negative_true_number_raises_error(self):
        """测试真数为负数抛出异常"""
        with pytest.raises(ValueError, match="对数的真数必须大于0"):
            ScientificCalculator.log(-5, 10)

    def test_log_invalid_base_zero_raises_error(self):
        """测试底为零抛出异常"""
        with pytest.raises(ValueError, match="对数的底必须大于0"):
            ScientificCalculator.log(10, 0)

    def test_log_invalid_base_negative_raises_error(self):
        """测试底为负数抛出异常"""
        with pytest.raises(ValueError, match="对数的底必须大于0"):
            ScientificCalculator.log(10, -2)

    def test_log_base_one_raises_error(self):
        """测试底为1抛出异常"""
        with pytest.raises(ValueError, match="对数的底不能为1"):
            ScientificCalculator.log(10, 1)

    def test_log_invalid_type_raises_error(self):
        """测试非数字类型抛出异常"""
        with pytest.raises(TypeError, match="参数必须是数字类型"):
            ScientificCalculator.log("10", 10)
        with pytest.raises(TypeError, match="参数必须是数字类型"):
            ScientificCalculator.log(10, "10")

    def test_log_custom_base(self):
        """测试自定义底的对数"""
        # log_3(27) = 3
        assert abs(ScientificCalculator.log(27, 3) - 3.0) < 1e-9
        # log_5(625) = 4
        assert abs(ScientificCalculator.log(625, 5) - 4.0) < 1e-9

    def test_log_small_positive_number(self):
        """测试接近零的正数对数"""
        result = ScientificCalculator.log(0.001, 10)
        assert abs(result - (-3.0)) < 1e-9

    def test_log_large_number(self):
        """测试大数字对数"""
        result = ScientificCalculator.log(1000000, 10)
        assert abs(result - 6.0) < 1e-9
