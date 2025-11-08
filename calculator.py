#!/usr/bin/env python3
"""
Простой калькулятор для демонстрации CI/CD процессов.
"""

import argparse
import sys


def add(a, b):
    """Сложение двух чисел."""
    return a + b


def subtract(a, b):
    """Вычитание двух чисел."""
    return a - b


def multiply(a, b):
    """Умножение двух чисел."""
    return a * b


def divide(a, b):
    """Деление двух чисел."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно!")
    return a / b


def power(a, b):
    """Возведение в степень."""
    return a**b


def main():
    """Основная функция CLI приложения."""
    parser = argparse.ArgumentParser(description="Простой калькулятор")
    parser.add_argument(
        "operation",
        choices=["add", "sub", "mul", "div", "pow"],
        help="Математическая операция",
    )
    parser.add_argument("a", type=float, help="Первое число")
    parser.add_argument("b", type=float, help="Второе число")

    args = parser.parse_args()

    operations = {
        "add": add,
        "sub": subtract,
        "mul": multiply,
        "div": divide,
        "pow": power,
    }

    try:
        result = operations[args.operation](args.a, args.b)
        print(f"Результат: {result}")
        return 0
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
