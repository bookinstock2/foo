import math


class ScientificCalculator:
    """
    A comprehensive scientific calculator class that provides basic arithmetic
    and advanced mathematical operations with proper error handling.

    This calculator supports addition, subtraction, multiplication, division,
    power operations, square root, and logarithmic calculations.
    """

    def add(self, a, b):
        """
        Add two numbers.

        Args:
            a: First number (int or float)
            b: Second number (int or float)

        Returns:
            float: The sum of a and b

        Raises:
            TypeError: If a or b is not a number

        Example:
            >>> calc = ScientificCalculator()
            >>> calc.add(5, 3)
            8
        """
        self._validate_numbers(a, b)
        return a + b

    def subtract(self, a, b):
        """
        Subtract two numbers.

        Args:
            a: First number (int or float)
            b: Second number (int or float)

        Returns:
            float: The difference of a and b

        Raises:
            TypeError: If a or b is not a number

        Example:
            >>> calc = ScientificCalculator()
            >>> calc.subtract(10, 3)
            7
        """
        self._validate_numbers(a, b)
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Args:
            a: First number (int or float)
            b: Second number (int or float)

        Returns:
            float: The product of a and b

        Raises:
            TypeError: If a or b is not a number

        Example:
            >>> calc = ScientificCalculator()
            >>> calc.multiply(4, 5)
            20
        """
        self._validate_numbers(a, b)
        return a * b

    def divide(self, a, b):
        """
        Divide two numbers.

        Args:
            a: Numerator (int or float)
            b: Denominator (int or float)

        Returns:
            float: The quotient of a divided by b

        Raises:
            TypeError: If a or b is not a number
            ZeroDivisionError: If b is zero

        Example:
            >>> calc = ScientificCalculator()
            >>> calc.divide(10, 2)
            5.0
        """
        self._validate_numbers(a, b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        """
        Calculate a to the power of b (a ** b).

        Args:
            a: Base number (int or float)
            b: Exponent (int or float)

        Returns:
            float: a raised to the power of b

        Raises:
            TypeError: If a or b is not a number
            ValueError: If the operation results in overflow

        Example:
            >>> calc = ScientificCalculator()
            >>> calc.power(2, 3)
            8.0
            >>> calc.power(4, 0.5)
            2.0
        """
        self._validate_numbers(a, b)
        try:
            result = a ** b
            return float(result)
        except OverflowError:
            raise ValueError("Power operation resulted in overflow")

    def sqrt(self, a):
        """
        Calculate the square root of a number.

        Args:
            a: Non-negative number (int or float)

        Returns:
            float: The square root of a

        Raises:
            TypeError: If a is not a number
            ValueError: If a is negative

        Example:
            >>> calc = ScientificCalculator()
            >>> calc.sqrt(16)
            4.0
            >>> calc.sqrt(2)
            1.4142135623730951
        """
        self._validate_single_number(a)
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(a)

    def log(self, a, base=10):
        """
        Calculate the logarithm of a number with a specified base.

        Args:
            a: Positive number (int or float)
            base: The logarithm base (int or float), default is 10

        Returns:
            float: The logarithm of a with the specified base

        Raises:
            TypeError: If a or base is not a number
            ValueError: If a is not positive or base is not positive/not equal to 1

        Example:
            >>> calc = ScientificCalculator()
            >>> calc.log(100)
            2.0
            >>> calc.log(8, 2)
            3.0
            >>> calc.log(20.085536923188)  # natural log base
            1.3010299956639813
        """
        self._validate_numbers(a, base)

        if a <= 0:
            raise ValueError("Cannot calculate logarithm of a non-positive number")
        if base <= 0:
            raise ValueError("Logarithm base must be positive")
        if base == 1:
            raise ValueError("Logarithm base cannot be 1")

        return math.log(a, base)

    def _validate_single_number(self, value):
        """
        Validate that a value is a number.

        Args:
            value: The value to validate

        Raises:
            TypeError: If value is not a number
        """
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError(f"Expected a number, got {type(value).__name__}")

    def _validate_numbers(self, *values):
        """
        Validate that all values are numbers.

        Args:
            *values: Variable number of values to validate

        Raises:
            TypeError: If any value is not a number
        """
        for value in values:
            self._validate_single_number(value)
