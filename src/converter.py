"""
单位转换工具类

提供多种单位转换功能，包括：
- 温度转换（摄氏度、华氏度、开尔文）
- 长度转换（米、英尺、英寸）
- 重量转换（千克、磅）
"""


class UnitConverter:
    """
    单位转换工具类

    提供各种常见的单位转换方法，支持温度、长度和重量的相互转换。
    所有方法都包含输入验证和适当的错误处理。
    """

    # 转换常量
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
    CELSIUS_TO_FAHRENHEIT_OFFSET = 32

    CELSIUS_TO_KELVIN_OFFSET = 273.15

    METERS_TO_FEET = 3.28084
    METERS_TO_INCHES = 39.3701

    KILOGRAMS_TO_POUNDS = 2.20462

    @staticmethod
    def _validate_temperature(value, name="temperature"):
        """
        验证温度值（适用于摄氏度和华氏度）

        Args:
            value: 温度值
            name: 参数名称，用于错误提示

        Raises:
            TypeError: 如果值不是数字
            ValueError: 如果值不是有效的数值
        """
        try:
            float_value = float(value)
            if not isinstance(float_value, (int, float)):
                raise TypeError(f"{name}必须是数字类型")
            return float_value
        except (TypeError, ValueError):
            raise TypeError(f"{name}必须是数字类型，收到: {type(value).__name__}")

    @staticmethod
    def _validate_kelvin(value, name="temperature"):
        """
        验证开尔文温度值（不能为负数）

        Args:
            value: 温度值（开尔文）
            name: 参数名称，用于错误提示

        Raises:
            TypeError: 如果值不是数字
            ValueError: 如果值是负数（违反热力学第二定律）
        """
        try:
            float_value = float(value)
            if float_value < 0:
                raise ValueError("开尔文温度不能为负数（不能低于绝对零度 0K）")
            return float_value
        except (TypeError, ValueError) as e:
            if isinstance(e, ValueError) and "不能为负数" in str(e):
                raise
            raise TypeError(f"{name}必须是数字类型，收到: {type(value).__name__}")

    @staticmethod
    def _validate_positive(value, name="value"):
        """
        验证正数值

        Args:
            value: 数值
            name: 参数名称，用于错误提示

        Raises:
            TypeError: 如果值不是数字
            ValueError: 如果值是负数
        """
        try:
            float_value = float(value)
            if float_value < 0:
                raise ValueError(f"{name}不能为负数，收到: {float_value}")
            return float_value
        except (TypeError, ValueError) as e:
            if isinstance(e, ValueError) and "不能为负数" in str(e):
                raise
            raise TypeError(f"{name}必须是数字类型，收到: {type(value).__name__}")

    # ==================== 温度转换方法 ====================

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """
        摄氏度转华氏度

        公式: F = C × 9/5 + 32

        Args:
            celsius (float): 摄氏度温度值

        Returns:
            float: 对应的华氏度温度值

        Raises:
            TypeError: 如果输入值不是数字类型

        Examples:
            >>> converter = UnitConverter()
            >>> converter.celsius_to_fahrenheit(0)
            32.0
            >>> converter.celsius_to_fahrenheit(100)
            212.0
            >>> converter.celsius_to_fahrenheit(-40)
            -40.0
        """
        celsius = UnitConverter._validate_temperature(celsius, "celsius")
        fahrenheit = celsius * UnitConverter.CELSIUS_TO_FAHRENHEIT_FACTOR + UnitConverter.CELSIUS_TO_FAHRENHEIT_OFFSET
        return round(fahrenheit, 2)

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """
        华氏度转摄氏度

        公式: C = (F - 32) × 5/9

        Args:
            fahrenheit (float): 华氏度温度值

        Returns:
            float: 对应的摄氏度温度值

        Raises:
            TypeError: 如果输入值不是数字类型

        Examples:
            >>> converter = UnitConverter()
            >>> converter.fahrenheit_to_celsius(32)
            0.0
            >>> converter.fahrenheit_to_celsius(212)
            100.0
            >>> converter.fahrenheit_to_celsius(-40)
            -40.0
        """
        fahrenheit = UnitConverter._validate_temperature(fahrenheit, "fahrenheit")
        celsius = (fahrenheit - UnitConverter.CELSIUS_TO_FAHRENHEIT_OFFSET) / UnitConverter.CELSIUS_TO_FAHRENHEIT_FACTOR
        return round(celsius, 2)

    @staticmethod
    def celsius_to_kelvin(celsius):
        """
        摄氏度转开尔文

        公式: K = C + 273.15

        Args:
            celsius (float): 摄氏度温度值

        Returns:
            float: 对应的开尔文温度值

        Raises:
            TypeError: 如果输入值不是数字类型
            ValueError: 如果转换后的开尔文温度为负数

        Examples:
            >>> converter = UnitConverter()
            >>> converter.celsius_to_kelvin(0)
            273.15
            >>> converter.celsius_to_kelvin(100)
            373.15
            >>> converter.celsius_to_kelvin(-273.15)
            0.0
        """
        celsius = UnitConverter._validate_temperature(celsius, "celsius")
        kelvin = celsius + UnitConverter.CELSIUS_TO_KELVIN_OFFSET

        # 验证结果不会低于绝对零度
        if kelvin < 0:
            raise ValueError(f"摄氏度 {celsius} 转换为开尔文后为负数，低于绝对零度 (0K)")

        return round(kelvin, 2)

    @staticmethod
    def kelvin_to_celsius(kelvin):
        """
        开尔文转摄氏度

        公式: C = K - 273.15

        Args:
            kelvin (float): 开尔文温度值，必须为非负数

        Returns:
            float: 对应的摄氏度温度值

        Raises:
            TypeError: 如果输入值不是数字类型
            ValueError: 如果输入值为负数

        Examples:
            >>> converter = UnitConverter()
            >>> converter.kelvin_to_celsius(273.15)
            0.0
            >>> converter.kelvin_to_celsius(373.15)
            100.0
            >>> converter.kelvin_to_celsius(0)
            -273.15
        """
        kelvin = UnitConverter._validate_kelvin(kelvin, "kelvin")
        celsius = kelvin - UnitConverter.CELSIUS_TO_KELVIN_OFFSET
        return round(celsius, 2)

    # ==================== 长度转换方法 ====================

    @staticmethod
    def meters_to_feet(meters):
        """
        米转英尺

        公式: feet = meters × 3.28084

        Args:
            meters (float): 米数，必须为非负数

        Returns:
            float: 对应的英尺数

        Raises:
            TypeError: 如果输入值不是数字类型
            ValueError: 如果输入值为负数

        Examples:
            >>> converter = UnitConverter()
            >>> converter.meters_to_feet(1)
            3.28
            >>> converter.meters_to_feet(10)
            32.81
        """
        meters = UnitConverter._validate_positive(meters, "meters")
        feet = meters * UnitConverter.METERS_TO_FEET
        return round(feet, 2)

    @staticmethod
    def feet_to_meters(feet):
        """
        英尺转米

        公式: meters = feet / 3.28084

        Args:
            feet (float): 英尺数，必须为非负数

        Returns:
            float: 对应的米数

        Raises:
            TypeError: 如果输入值不是数字类型
            ValueError: 如果输入值为负数

        Examples:
            >>> converter = UnitConverter()
            >>> converter.feet_to_meters(3.28084)
            1.0
            >>> converter.feet_to_meters(32.8084)
            10.0
        """
        feet = UnitConverter._validate_positive(feet, "feet")
        meters = feet / UnitConverter.METERS_TO_FEET
        return round(meters, 2)

    @staticmethod
    def meters_to_inches(meters):
        """
        米转英寸

        公式: inches = meters × 39.3701

        Args:
            meters (float): 米数，必须为非负数

        Returns:
            float: 对应的英寸数

        Raises:
            TypeError: 如果输入值不是数字类型
            ValueError: 如果输入值为负数

        Examples:
            >>> converter = UnitConverter()
            >>> converter.meters_to_inches(1)
            39.37
            >>> converter.meters_to_inches(0.1)
            3.94
        """
        meters = UnitConverter._validate_positive(meters, "meters")
        inches = meters * UnitConverter.METERS_TO_INCHES
        return round(inches, 2)

    # ==================== 重量转换方法 ====================

    @staticmethod
    def kilograms_to_pounds(kilograms):
        """
        千克转磅

        公式: pounds = kilograms × 2.20462

        Args:
            kilograms (float): 千克数，必须为非负数

        Returns:
            float: 对应的磅数

        Raises:
            TypeError: 如果输入值不是数字类型
            ValueError: 如果输入值为负数

        Examples:
            >>> converter = UnitConverter()
            >>> converter.kilograms_to_pounds(1)
            2.2
            >>> converter.kilograms_to_pounds(70)
            154.32
        """
        kilograms = UnitConverter._validate_positive(kilograms, "kilograms")
        pounds = kilograms * UnitConverter.KILOGRAMS_TO_POUNDS
        return round(pounds, 2)

    @staticmethod
    def pounds_to_kilograms(pounds):
        """
        磅转千克

        公式: kilograms = pounds / 2.20462

        Args:
            pounds (float): 磅数，必须为非负数

        Returns:
            float: 对应的千克数

        Raises:
            TypeError: 如果输入值不是数字类型
            ValueError: 如果输入值为负数

        Examples:
            >>> converter = UnitConverter()
            >>> converter.pounds_to_kilograms(2.20462)
            1.0
            >>> converter.pounds_to_kilograms(154.32)
            70.0
        """
        pounds = UnitConverter._validate_positive(pounds, "pounds")
        kilograms = pounds / UnitConverter.KILOGRAMS_TO_POUNDS
        return round(kilograms, 2)


if __name__ == "__main__":
    # 使用示例
    converter = UnitConverter()

    print("=== 温度转换示例 ===")
    print(f"0°C = {converter.celsius_to_fahrenheit(0)}°F")
    print(f"100°C = {converter.celsius_to_fahrenheit(100)}°F")
    print(f"212°F = {converter.fahrenheit_to_celsius(212)}°C")
    print(f"0°C = {converter.celsius_to_kelvin(0)}K")
    print(f"273.15K = {converter.kelvin_to_celsius(273.15)}°C")

    print("\n=== 长度转换示例 ===")
    print(f"1米 = {converter.meters_to_feet(1)}英尺")
    print(f"10英尺 = {converter.feet_to_meters(10)}米")
    print(f"1米 = {converter.meters_to_inches(1)}英寸")

    print("\n=== 重量转换示例 ===")
    print(f"1千克 = {converter.kilograms_to_pounds(1)}磅")
    print(f"70千克 = {converter.kilograms_to_pounds(70)}磅")
    print(f"154.32磅 = {converter.pounds_to_kilograms(154.32)}千克")

    print("\n=== 错误处理示例 ===")
    try:
        converter.celsius_to_kelvin(-300)
    except ValueError as e:
        print(f"错误捕获: {e}")

    try:
        converter.meters_to_feet(-5)
    except ValueError as e:
        print(f"错误捕获: {e}")

    try:
        converter.kilograms_to_pounds("abc")
    except TypeError as e:
        print(f"错误捕获: {e}")
