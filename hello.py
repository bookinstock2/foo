def hello(name: str = "World") -> str:
    """
    返回一个问候语

    Args:
        name: 被问候的人的名字，默认为 "World"

    Returns:
        问候字符串
    """
    return f"Hello, {name}!"
