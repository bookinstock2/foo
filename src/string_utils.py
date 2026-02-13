"""字符串处理工具模块"""


def reverse_string(s):
    """反转字符串

    Args:
        s: 输入字符串

    Returns:
        反转后的字符串
    """
    if not isinstance(s, str):
        raise TypeError("输入必须是字符串")
    return s[::-1]


def count_vowels(s):
    """统计元音字母数量

    Args:
        s: 输入字符串

    Returns:
        元音字母的数量
    """
    if not isinstance(s, str):
        raise TypeError("输入必须是字符串")

    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def to_camel_case(s):
    """将 snake_case 转为 camelCase

    Args:
        s: snake_case 格式的字符串

    Returns:
        camelCase 格式的字符串
    """
    if not isinstance(s, str):
        raise TypeError("输入必须是字符串")

    if not s:
        return s

    parts = s.split("_")
    # 第一个单词转为小写，后续单词首字母大写
    if parts:
        parts[0] = parts[0].lower()
    return "".join(word.capitalize() if i > 0 else parts[i] for i, word in enumerate(parts))
