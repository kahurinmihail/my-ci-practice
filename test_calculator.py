#!/usr/bin/env python3
"""
Тесты для калькулятора.
"""

from unittest.mock import patch

import pytest

from calculator import add, divide, main, multiply, power, subtract


class TestCalculatorFunctions:
    """Тесты для математических функций калькулятора."""

    def test_add(self):
        """Тест функции сложения."""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(1.5, 2.5) == 4.0

    def test_subtract(self):
        """Тест функции вычитания."""
        assert subtract(5, 3) == 2
        assert subtract(1, 1) == 0
        assert subtract(0, 5) == -5
        assert subtract(2.5, 1.5) == 1.0

    def test_multiply(self):
        """Тест функции умножения."""
        assert multiply(2, 3) == 6
        assert multiply(-2, 3) == -6
        assert multiply(0, 5) == 0
        assert multiply(1.5, 2) == 3.0

    def test_divide(self):
        """Тест функции деления."""
        assert divide(6, 2) == 3
        assert divide(5, 2) == 2.5
        assert divide(-6, 2) == -3
        assert divide(0, 5) == 0

    def test_divide_by_zero(self):
        """Тест деления на ноль."""
        with pytest.raises(ValueError, match="Деление на ноль невозможно!"):
            divide(5, 0)

    def test_power(self):
        """Тест функции возведения в степень."""
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(3, 2) == 9
        assert power(2, -1) == 0.5


class TestEdgeCases:
    """Тесты граничных случаев."""

    def test_large_numbers(self):
        """Тест с большими числами."""
        assert add(1000000, 2000000) == 3000000
        assert multiply(1000, 1000) == 1000000

    def test_floating_point_precision(self):
        """Тест точности с плавающей точкой."""
        result = add(0.1, 0.2)
        assert abs(result - 0.3) < 1e-10

    def test_negative_numbers(self):
        """Тест с отрицательными числами."""
        assert add(-5, -3) == -8
        assert subtract(-5, -3) == -2
        assert multiply(-2, -3) == 6
        assert divide(-6, -2) == 3


class TestCLIInterface:
    """Тесты CLI интерфейса для увеличения покрытия кода."""

    @patch("sys.argv", ["calculator.py", "add", "5", "3"])
    def test_cli_add_success(self, capsys):
        """Тест успешного выполнения CLI команды сложения."""
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Результат: 8.0" in captured.out

    @patch("sys.argv", ["calculator.py", "div", "10", "2"])
    def test_cli_div_success(self, capsys):
        """Тест успешного выполнения CLI команды деления."""
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Результат: 5.0" in captured.out

    @patch("sys.argv", ["calculator.py", "div", "5", "0"])
    def test_cli_division_by_zero(self, capsys):
        """Тест обработки деления на ноль в CLI."""
        result = main()
        captured = capsys.readouterr()
        assert result == 1
        assert "Ошибка: Деление на ноль невозможно!" in captured.err

    @patch("sys.argv", ["calculator.py", "mul", "4", "7"])
    def test_cli_multiply_success(self, capsys):
        """Тест успешного выполнения CLI команды умножения."""
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Результат: 28.0" in captured.out
