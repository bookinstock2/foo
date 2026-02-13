"""字符串处理工具的单元测试"""

import unittest
from src.string_utils import reverse_string, count_vowels, to_camel_case


class TestReverseString(unittest.TestCase):
    """reverse_string 函数的测试类"""

    def test_reverse_simple_string(self):
        """测试简单字符串反转"""
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_empty_string(self):
        """测试空字符串"""
        self.assertEqual(reverse_string(""), "")

    def test_reverse_single_character(self):
        """测试单个字符"""
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_with_spaces(self):
        """测试包含空格的字符串"""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_reverse_with_numbers(self):
        """测试包含数字的字符串"""
        self.assertEqual(reverse_string("abc123"), "321cba")

    def test_reverse_with_special_characters(self):
        """测试包含特殊字符的字符串"""
        self.assertEqual(reverse_string("hello!@#"), "#@!olleh")

    def test_reverse_palindrome(self):
        """测试回文字符串"""
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_reverse_unicode_characters(self):
        """测试 Unicode 字符"""
        self.assertEqual(reverse_string("你好"), "好你")

    def test_reverse_mixed_case(self):
        """测试混合大小写"""
        self.assertEqual(reverse_string("HeLLo"), "oLLeH")

    def test_reverse_non_string_input_raises_error(self):
        """测试非字符串输入抛出异常"""
        with self.assertRaises(TypeError):
            reverse_string(123)

    def test_reverse_none_input_raises_error(self):
        """测试 None 输入抛出异常"""
        with self.assertRaises(TypeError):
            reverse_string(None)

    def test_reverse_list_input_raises_error(self):
        """测试列表输入抛出异常"""
        with self.assertRaises(TypeError):
            reverse_string(["a", "b"])


class TestCountVowels(unittest.TestCase):
    """count_vowels 函数的测试类"""

    def test_count_vowels_simple_string(self):
        """测试简单字符串的元音计数"""
        self.assertEqual(count_vowels("hello"), 2)

    def test_count_vowels_empty_string(self):
        """测试空字符串"""
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_no_vowels(self):
        """测试没有元音的字符串"""
        self.assertEqual(count_vowels("xyz"), 0)

    def test_count_vowels_all_vowels(self):
        """测试全是元音的字符串"""
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_count_vowels_uppercase_vowels(self):
        """测试大写元音"""
        self.assertEqual(count_vowels("HELLO"), 2)

    def test_count_vowels_mixed_case_vowels(self):
        """测试混合大小写元音"""
        self.assertEqual(count_vowels("HeLLo"), 2)

    def test_count_vowels_with_numbers_and_spaces(self):
        """测试包含数字和空格的字符串"""
        self.assertEqual(count_vowels("hello 123 world"), 3)

    def test_count_vowels_with_special_characters(self):
        """测试包含特殊字符的字符串"""
        self.assertEqual(count_vowels("h@e!l*l&o"), 2)

    def test_count_vowels_single_vowel(self):
        """测试单个元音"""
        self.assertEqual(count_vowels("a"), 1)

    def test_count_vowels_single_consonant(self):
        """测试单个辅音"""
        self.assertEqual(count_vowels("b"), 0)

    def test_count_vowels_repeated_vowels(self):
        """测试重复的元音"""
        self.assertEqual(count_vowels("aaa"), 3)

    def test_count_vowels_unicode_string(self):
        """测试 Unicode 字符串"""
        self.assertEqual(count_vowels("你好ai世界"), 2)

    def test_count_vowels_non_string_input_raises_error(self):
        """测试非字符串输入抛出异常"""
        with self.assertRaises(TypeError):
            count_vowels(123)

    def test_count_vowels_none_input_raises_error(self):
        """测试 None 输入抛出异常"""
        with self.assertRaises(TypeError):
            count_vowels(None)

    def test_count_vowels_list_input_raises_error(self):
        """测试列表输入抛出异常"""
        with self.assertRaises(TypeError):
            count_vowels(["a", "e"])


class TestToCamelCase(unittest.TestCase):
    """to_camel_case 函数的测试类"""

    def test_camel_case_simple_conversion(self):
        """测试简单的 snake_case 转 camelCase"""
        self.assertEqual(to_camel_case("hello_world"), "helloWorld")

    def test_camel_case_empty_string(self):
        """测试空字符串"""
        self.assertEqual(to_camel_case(""), "")

    def test_camel_case_single_word(self):
        """测试单个单词"""
        self.assertEqual(to_camel_case("hello"), "hello")

    def test_camel_case_multiple_underscores(self):
        """测试多个下划线"""
        self.assertEqual(to_camel_case("hello_world_foo_bar"), "helloWorldFooBar")

    def test_camel_case_with_numbers(self):
        """测试包含数字的转换"""
        self.assertEqual(to_camel_case("hello_world_123"), "helloWorld123")

    def test_camel_case_uppercase_input(self):
        """测试大写字符转换"""
        self.assertEqual(to_camel_case("HELLO_WORLD"), "helloWorld")

    def test_camel_case_mixed_case_input(self):
        """测试混合大小写转换"""
        self.assertEqual(to_camel_case("Hello_World"), "helloWorld")

    def test_camel_case_leading_underscore(self):
        """测试以下划线开头的字符串"""
        self.assertEqual(to_camel_case("_hello_world"), "HelloWorld")

    def test_camel_case_trailing_underscore(self):
        """测试以下划线结尾的字符串"""
        self.assertEqual(to_camel_case("hello_world_"), "helloWorld")

    def test_camel_case_multiple_consecutive_underscores(self):
        """测试连续的下划线"""
        self.assertEqual(to_camel_case("hello__world"), "helloWorld")

    def test_camel_case_single_underscore(self):
        """测试只有下划线"""
        self.assertEqual(to_camel_case("_"), "")

    def test_camel_case_non_string_input_raises_error(self):
        """测试非字符串输入抛出异常"""
        with self.assertRaises(TypeError):
            to_camel_case(123)

    def test_camel_case_none_input_raises_error(self):
        """测试 None 输入抛出异常"""
        with self.assertRaises(TypeError):
            to_camel_case(None)

    def test_camel_case_list_input_raises_error(self):
        """测试列表输入抛出异常"""
        with self.assertRaises(TypeError):
            to_camel_case(["hello", "world"])

    def test_camel_case_with_special_characters(self):
        """测试包含特殊字符的转换"""
        self.assertEqual(to_camel_case("hello@world"), "hello@world")


if __name__ == "__main__":
    unittest.main(verbosity=2)
