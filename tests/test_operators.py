"""
Tests unitaires du module operators.py.

Ces tests valident le comportement attendu des opérations arithmétiques.
S'ils échouent, cela indique probablement un bogue dans la logique métier.
"""

import pytest

# Ajuste l'import selon votre structure:
# - Si operators.py est dans src/: from src.operators import ...
# - Sinon (à la racine): from operators import ...
from src.operators import add, subtract, multiply, divide


def test_add_basic():
    """add(a, b) doit retourner la somme a + b."""
    assert add(2, 3) == 5


def test_add_decimal():
    """add(a, b) doit supporter les nombres décimaux."""
    assert add(2.5, 0.5) == 3.0


def test_subtract_basic():
    """subtract(a, b) doit retourner a - b."""
    assert subtract(10, 4) == 6


def test_multiply_basic():
    """multiply(a, b) doit retourner a * b."""
    assert multiply(6, 7) == 42


def test_divide_basic():
    """divide(a, b) doit retourner a / b (division réelle)."""
    assert divide(12, 3) == 4


def test_divide_decimal_result():
    """divide(a, b) doit retourner un résultat décimal si nécessaire."""
    assert divide(5, 2) == 2.5


def test_divide_by_zero_raises():
    """divide(a, b) doit lever une exception quand b == 0."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)