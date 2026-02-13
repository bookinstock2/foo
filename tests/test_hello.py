import pytest
from hello import hello


class TestHello:
    """Hello 函数的测试类"""

    def test_hello_default(self):
        """测试默认参数情况"""
        assert hello() == "Hello, World!"

    def test_hello_with_name(self):
        """测试带名字的情况"""
        assert hello("Alice") == "Hello, Alice!"

    def test_hello_with_empty_string(self):
        """测试空字符串"""
        assert hello("") == "Hello, !"

    def test_hello_with_special_characters(self):
        """测试特殊字符"""
        assert hello("World!@#") == "Hello, World!@#!"
