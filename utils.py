from datetime import datetime


def format_date(date: datetime) -> str:
    """
    将 datetime 对象格式化为 YYYY-MM-DD 格式的字符串。

    Args:
        date: datetime 对象

    Returns:
        YYYY-MM-DD 格式的日期字符串
    """
    return date.strftime("%Y-%m-%d")


def is_palindrome(s: str) -> bool:
    """
    判断字符串是否为回文。

    Args:
        s: 待检查的字符串

    Returns:
        如果是回文返回 True，否则返回 False
    """
    # 移除空格和特殊字符，转换为小写进行比较
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
