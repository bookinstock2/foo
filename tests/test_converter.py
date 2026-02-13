"""单位转换工具测试模块"""

import pytest
from converter import UnitConverter


class TestTemperatureConversion:
    """温度转换的测试类"""

    # Celsius to Fahrenheit 转换测试
    def test_celsius_to_fahrenheit_freezing_point(self):
        """测试摄氏度转华氏度 - 冰点"""
        assert UnitConverter.celsius_to_fahrenheit(0) == 32

    def test_celsius_to_fahrenheit_boiling_point(self):
        """测试摄氏度转华氏度 - 沸点"""
        assert UnitConverter.celsius_to_fahrenheit(100) == 212

    def test_celsius_to_fahrenheit_negative(self):
        """测试摄氏度转华氏度 - 负温度"""
        assert UnitConverter.celsius_to_fahrenheit(-40) == -40

    def test_celsius_to_fahrenheit_positive(self):
        """测试摄氏度转华氏度 - 正温度"""
        assert abs(UnitConverter.celsius_to_fahrenheit(20) - 68) < 1e-9

    def test_celsius_to_fahrenheit_body_temperature(self):
        """测试摄氏度转华氏度 - 体温"""
        assert abs(UnitConverter.celsius_to_fahrenheit(37) - 98.6) < 1e-9

    # Fahrenheit to Celsius 转换测试
    def test_fahrenheit_to_celsius_freezing_point(self):
        """测试华氏度转摄氏度 - 冰点"""
        assert UnitConverter.fahrenheit_to_celsius(32) == 0

    def test_fahrenheit_to_celsius_boiling_point(self):
        """测试华氏度转摄氏度 - 沸点"""
        assert UnitConverter.fahrenheit_to_celsius(212) == 100

    def test_fahrenheit_to_celsius_negative(self):
        """测试华氏度转摄氏度 - 负温度"""
        assert UnitConverter.fahrenheit_to_celsius(-40) == -40

    def test_fahrenheit_to_celsius_positive(self):
        """测试华氏度转摄氏度 - 正温度"""
        assert abs(UnitConverter.fahrenheit_to_celsius(68) - 20) < 1e-9

    # 相互转换一致性测试
    def test_temperature_roundtrip_celsius_fahrenheit(self):
        """测试温度转换往返一致性 C->F->C"""
        original = 25
        converted = UnitConverter.celsius_to_fahrenheit(original)
        back = UnitConverter.fahrenheit_to_celsius(converted)
        assert abs(original - back) < 1e-9, \
            f"往返转换应该相等: 原值={original}, 往返后={back}"

    def test_temperature_roundtrip_fahrenheit_celsius(self):
        """测试温度转换往返一致性 F->C->F"""
        original = 98.6
        converted = UnitConverter.fahrenheit_to_celsius(original)
        back = UnitConverter.celsius_to_fahrenheit(converted)
        assert abs(original - back) < 1e-9, \
            f"往返转换应该相等: 原值={original}, 往返后={back}"

    # Celsius to Kelvin 转换测试
    def test_celsius_to_kelvin_absolute_zero(self):
        """测试摄氏度转开尔文 - 绝对零度"""
        assert abs(UnitConverter.celsius_to_kelvin(-273.15) - 0) < 1e-9

    def test_celsius_to_kelvin_freezing_point(self):
        """测试摄氏度转开尔文 - 冰点"""
        assert abs(UnitConverter.celsius_to_kelvin(0) - 273.15) < 1e-9

    def test_celsius_to_kelvin_room_temperature(self):
        """测试摄氏度转开尔文 - 室温"""
        assert abs(UnitConverter.celsius_to_kelvin(25) - 298.15) < 1e-9

    def test_celsius_to_kelvin_below_absolute_zero_raises_error(self):
        """测试摄氏度转开尔文 - 低于绝对零度抛出异常"""
        with pytest.raises(ValueError, match="温度不能低于绝对零度"):
            UnitConverter.celsius_to_kelvin(-300)

    # Kelvin to Celsius 转换测试
    def test_kelvin_to_celsius_absolute_zero(self):
        """测试开尔文转摄氏度 - 绝对零度"""
        assert abs(UnitConverter.kelvin_to_celsius(0) - (-273.15)) < 1e-9

    def test_kelvin_to_celsius_freezing_point(self):
        """测试开尔文转摄氏度 - 冰点"""
        assert abs(UnitConverter.kelvin_to_celsius(273.15) - 0) < 1e-9

    def test_kelvin_to_celsius_room_temperature(self):
        """测试开尔文转摄氏度 - 室温"""
        assert abs(UnitConverter.kelvin_to_celsius(298.15) - 25) < 1e-9

    def test_kelvin_to_celsius_negative_raises_error(self):
        """测试开尔文转摄氏度 - 负数抛出异常"""
        with pytest.raises(ValueError, match="开尔文温度不能为负数"):
            UnitConverter.kelvin_to_celsius(-5)

    # 温度转换无效输入测试
    def test_celsius_to_fahrenheit_invalid_type(self):
        """测试温度转换 - 无效的类型"""
        with pytest.raises(TypeError, match="温度值必须是数字类型"):
            UnitConverter.celsius_to_fahrenheit("20")

    def test_fahrenheit_to_celsius_invalid_type(self):
        """测试温度转换 - 无效的类型"""
        with pytest.raises(TypeError, match="温度值必须是数字类型"):
            UnitConverter.fahrenheit_to_celsius("68")

    def test_celsius_to_kelvin_invalid_type(self):
        """测试温度转换 - 无效的类型"""
        with pytest.raises(TypeError, match="温度值必须是数字类型"):
            UnitConverter.celsius_to_kelvin([0])

    def test_kelvin_to_celsius_invalid_type(self):
        """测试温度转换 - 无效的类型"""
        with pytest.raises(TypeError, match="温度值必须是数字类型"):
            UnitConverter.kelvin_to_celsius({"k": 273.15})


class TestLengthConversion:
    """长度转换的测试类"""

    # Meters to Feet 转换测试
    def test_meters_to_feet_zero(self):
        """测试米转英尺 - 零"""
        assert UnitConverter.meters_to_feet(0) == 0

    def test_meters_to_feet_one_meter(self):
        """测试米转英尺 - 1米"""
        assert abs(UnitConverter.meters_to_feet(1) - 3.28084) < 1e-4

    def test_meters_to_feet_standard(self):
        """测试米转英尺 - 标准转换"""
        assert abs(UnitConverter.meters_to_feet(10) - 32.8084) < 1e-4

    def test_meters_to_feet_decimal(self):
        """测试米转英尺 - 小数"""
        assert abs(UnitConverter.meters_to_feet(0.5) - 1.64042) < 1e-4

    def test_meters_to_feet_negative_raises_error(self):
        """测试米转英尺 - 负数抛出异常"""
        with pytest.raises(ValueError, match="长度不能为负数"):
            UnitConverter.meters_to_feet(-5)

    # Feet to Meters 转换测试
    def test_feet_to_meters_zero(self):
        """测试英尺转米 - 零"""
        assert UnitConverter.feet_to_meters(0) == 0

    def test_feet_to_meters_one_foot(self):
        """测试英尺转米 - 1英尺"""
        assert abs(UnitConverter.feet_to_meters(1) - 0.3048) < 1e-4

    def test_feet_to_meters_standard(self):
        """测试英尺转米 - 标准转换"""
        assert abs(UnitConverter.feet_to_meters(32.8084) - 10) < 1e-4

    def test_feet_to_meters_negative_raises_error(self):
        """测试英尺转米 - 负数抛出异常"""
        with pytest.raises(ValueError, match="长度不能为负数"):
            UnitConverter.feet_to_meters(-10)

    # Kilometers to Miles 转换测试
    def test_kilometers_to_miles_zero(self):
        """测试公里转英里 - 零"""
        assert UnitConverter.kilometers_to_miles(0) == 0

    def test_kilometers_to_miles_standard(self):
        """测试公里转英里 - 标准转换"""
        assert abs(UnitConverter.kilometers_to_miles(1) - 0.621371) < 1e-5

    def test_kilometers_to_miles_long_distance(self):
        """测试公里转英里 - 长距离"""
        assert abs(UnitConverter.kilometers_to_miles(100) - 62.1371) < 1e-3

    def test_kilometers_to_miles_decimal(self):
        """测试公里转英里 - 小数"""
        assert abs(UnitConverter.kilometers_to_miles(1.5) - 0.932057) < 1e-5

    def test_kilometers_to_miles_negative_raises_error(self):
        """测试公里转英里 - 负数抛出异常"""
        with pytest.raises(ValueError, match="长度不能为负数"):
            UnitConverter.kilometers_to_miles(-50)

    # Miles to Kilometers 转换测试
    def test_miles_to_kilometers_zero(self):
        """测试英里转公里 - 零"""
        assert UnitConverter.miles_to_kilometers(0) == 0

    def test_miles_to_kilometers_standard(self):
        """测试英里转公里 - 标准转换"""
        assert abs(UnitConverter.miles_to_kilometers(1) - 1.60934) < 1e-4

    def test_miles_to_kilometers_long_distance(self):
        """测试英里转公里 - 长距离"""
        assert abs(UnitConverter.miles_to_kilometers(62.1371) - 100) < 1e-3

    def test_miles_to_kilometers_negative_raises_error(self):
        """测试英里转公里 - 负数抛出异常"""
        with pytest.raises(ValueError, match="长度不能为负数"):
            UnitConverter.miles_to_kilometers(-100)

    # 长度转换往返一致性
    def test_length_roundtrip_meters_feet(self):
        """测试长度转换往返一致性 m->ft->m"""
        original = 50
        converted = UnitConverter.meters_to_feet(original)
        back = UnitConverter.feet_to_meters(converted)
        assert abs(original - back) < 1e-9, \
            f"往返转换应该相等: 原值={original}m, 往返后={back}m"

    def test_length_roundtrip_kilometers_miles(self):
        """测试长度转换往返一致性 km->mi->km"""
        original = 100
        converted = UnitConverter.kilometers_to_miles(original)
        back = UnitConverter.miles_to_kilometers(converted)
        assert abs(original - back) < 1e-9, \
            f"往返转换应该相等: 原值={original}km, 往返后={back}km"

    # 长度转换无效输入
    def test_meters_to_feet_invalid_type(self):
        """测试长度转换 - 无效的类型"""
        with pytest.raises(TypeError, match="长度值必须是数字类型"):
            UnitConverter.meters_to_feet("10")

    def test_kilometers_to_miles_invalid_type(self):
        """测试长度转换 - 无效的类型"""
        with pytest.raises(TypeError, match="长度值必须是数字类型"):
            UnitConverter.kilometers_to_miles([100])


class TestWeightConversion:
    """重量转换的测试类"""

    # Kilograms to Pounds 转换测试
    def test_kilograms_to_pounds_zero(self):
        """测试公斤转磅 - 零"""
        assert UnitConverter.kilograms_to_pounds(0) == 0

    def test_kilograms_to_pounds_standard(self):
        """测试公斤转磅 - 1公斤"""
        assert abs(UnitConverter.kilograms_to_pounds(1) - 2.20462) < 1e-4

    def test_kilograms_to_pounds_body_weight(self):
        """测试公斤转磅 - 体重"""
        assert abs(UnitConverter.kilograms_to_pounds(70) - 154.324) < 1e-2

    def test_kilograms_to_pounds_decimal(self):
        """测试公斤转磅 - 小数"""
        assert abs(UnitConverter.kilograms_to_pounds(2.5) - 5.51155) < 1e-4

    def test_kilograms_to_pounds_negative_raises_error(self):
        """测试公斤转磅 - 负数抛出异常"""
        with pytest.raises(ValueError, match="重量不能为负数"):
            UnitConverter.kilograms_to_pounds(-10)

    # Pounds to Kilograms 转换测试
    def test_pounds_to_kilograms_zero(self):
        """测试磅转公斤 - 零"""
        assert UnitConverter.pounds_to_kilograms(0) == 0

    def test_pounds_to_kilograms_standard(self):
        """测试磅转公斤 - 1磅"""
        assert abs(UnitConverter.pounds_to_kilograms(1) - 0.453592) < 1e-5

    def test_pounds_to_kilograms_body_weight(self):
        """测试磅转公斤 - 体重"""
        assert abs(UnitConverter.pounds_to_kilograms(154.324) - 70) < 1e-2

    def test_pounds_to_kilograms_decimal(self):
        """测试磅转公斤 - 小数"""
        assert abs(UnitConverter.pounds_to_kilograms(5.51155) - 2.5) < 1e-4

    def test_pounds_to_kilograms_negative_raises_error(self):
        """测试磅转公斤 - 负数抛出异常"""
        with pytest.raises(ValueError, match="重量不能为负数"):
            UnitConverter.pounds_to_kilograms(-50)

    # Grams to Ounces 转换测试
    def test_grams_to_ounces_zero(self):
        """测试克转盎司 - 零"""
        assert UnitConverter.grams_to_ounces(0) == 0

    def test_grams_to_ounces_standard(self):
        """测试克转盎司 - 标准转换"""
        assert abs(UnitConverter.grams_to_ounces(28.3495) - 1) < 1e-4

    def test_grams_to_ounces_decimal(self):
        """测试克转盎司 - 小数"""
        assert abs(UnitConverter.grams_to_ounces(100) - 3.52740) < 1e-4

    def test_grams_to_ounces_large(self):
        """测试克转盎司 - 大数字"""
        assert abs(UnitConverter.grams_to_ounces(1000) - 35.2740) < 1e-3

    def test_grams_to_ounces_negative_raises_error(self):
        """测试克转盎司 - 负数抛出异常"""
        with pytest.raises(ValueError, match="重量不能为负数"):
            UnitConverter.grams_to_ounces(-100)

    # Ounces to Grams 转换测试
    def test_ounces_to_grams_zero(self):
        """测试盎司转克 - 零"""
        assert UnitConverter.ounces_to_grams(0) == 0

    def test_ounces_to_grams_standard(self):
        """测试盎司转克 - 1盎司"""
        assert abs(UnitConverter.ounces_to_grams(1) - 28.3495) < 1e-3

    def test_ounces_to_grams_decimal(self):
        """测试盎司转克 - 小数"""
        assert abs(UnitConverter.ounces_to_grams(3.52740) - 100) < 1e-3

    def test_ounces_to_grams_large(self):
        """测试盎司转克 - 大数字"""
        assert abs(UnitConverter.ounces_to_grams(35.2740) - 1000) < 1e-2

    def test_ounces_to_grams_negative_raises_error(self):
        """测试盎司转克 - 负数抛出异常"""
        with pytest.raises(ValueError, match="重量不能为负数"):
            UnitConverter.ounces_to_grams(-10)

    # 重量转换往返一致性
    def test_weight_roundtrip_kilograms_pounds(self):
        """测试重量转换往返一致性 kg->lb->kg"""
        original = 100
        converted = UnitConverter.kilograms_to_pounds(original)
        back = UnitConverter.pounds_to_kilograms(converted)
        assert abs(original - back) < 1e-9, \
            f"往返转换应该相等: 原值={original}kg, 往返后={back}kg"

    def test_weight_roundtrip_grams_ounces(self):
        """测试重量转换往返一致性 g->oz->g"""
        original = 500
        converted = UnitConverter.grams_to_ounces(original)
        back = UnitConverter.ounces_to_grams(converted)
        assert abs(original - back) < 1e-9, \
            f"往返转换应该相等: 原值={original}g, 往返后={back}g"

    # 重量转换无效输入
    def test_kilograms_to_pounds_invalid_type(self):
        """测试重量转换 - 无效的类型"""
        with pytest.raises(TypeError, match="重量值必须是数字类型"):
            UnitConverter.kilograms_to_pounds("70")

    def test_grams_to_ounces_invalid_type(self):
        """测试重量转换 - 无效的类型"""
        with pytest.raises(TypeError, match="重量值必须是数字类型"):
            UnitConverter.grams_to_ounces(None)

    def test_pounds_to_kilograms_invalid_type(self):
        """测试重量转换 - 无效的类型"""
        with pytest.raises(TypeError, match="重量值必须是数字类型"):
            UnitConverter.pounds_to_kilograms({"lb": 154.324})

    def test_ounces_to_grams_invalid_type(self):
        """测试重量转换 - 无效的类型"""
        with pytest.raises(TypeError, match="重量值必须是数字类型"):
            UnitConverter.ounces_to_grams([35.274])
