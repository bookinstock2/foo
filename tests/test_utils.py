import pytest
from datetime import datetime
from utils import format_date, is_palindrome


class TestFormatDate:
    """format_date 函数的测试类"""

    def test_format_date_standard(self):
        """测试标准日期格式"""
        date = datetime(2024, 2, 13)
        assert format_date(date) == "2024-02-13"

    def test_format_date_january(self):
        """测试一月份"""
        date = datetime(2024, 1, 1)
        assert format_date(date) == "2024-01-01"

    def test_format_date_december(self):
        """测试十二月份"""
        date = datetime(2024, 12, 31)
        assert format_date(date) == "2024-12-31"

    def test_format_date_with_time(self):
        """测试包含时间的日期"""
        date = datetime(2024, 2, 13, 15, 30, 45)
        assert format_date(date) == "2024-02-13"


class TestIsPalindrome:
    """is_palindrome 函数的测试类"""

    def test_palindrome_simple(self):
        """测试简单回文"""
        assert is_palindrome("aba") is True

    def test_palindrome_with_spaces(self):
        """测试包含空格的回文"""
        assert is_palindrome("a b a") is True

    def test_palindrome_case_insensitive(self):
        """测试大小写不敏感"""
        assert is_palindrome("Aba") is True

    def test_palindrome_with_special_chars(self):
        """测试包含特殊字符的回文"""
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_not_palindrome(self):
        """测试非回文"""
        assert is_palindrome("hello") is False

    def test_single_character(self):
        """测试单个字符"""
        assert is_palindrome("a") is True

    def test_empty_string(self):
        """测试空字符串"""
        assert is_palindrome("") is True

    def test_two_character_palindrome(self):
        """测试两字符回文"""
        assert is_palindrome("aa") is True

    def test_two_character_not_palindrome(self):
        """测试两字符非回文"""
        assert is_palindrome("ab") is False

    def test_palindrome_with_numbers(self):
        """测试包含数字的回文"""
        assert is_palindrome("12321") is True

    def test_mixed_alphanumeric(self):
        """测试混合字母和数字的回文"""
        assert is_palindrome("A1b1A") is True
