import sys
from pathlib import Path
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add, subtract, multiply, divide, square, sin, cos, tan, square_root, percentage

def test_add_correct():
    assert add(5, 6) == 11

def test_add_wrong():
    assert add(5, 6) != 10


def test_subtract_correct():
    assert subtract(10, 5) == 5

def test_subtract_wrong():
    assert subtract(10, 5) != 6


def test_multiply_correct():
    assert multiply(4, 5) == 20

def test_multiply_wrong():
    assert multiply(4, 5) != 21


def test_divide_correct():
    assert divide(20, 4) == 5

def test_divide_wrong():
    assert divide(20, 4) != 6


def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_squre_correct():
    assert square(6) == 36

def test_square_wrong():
    assert square(6) != 35

def test_sin_correct():
    assert sin(math.pi/2) == 1

def test_cos_correct():
    assert cos(0) == 1

def test_tan_correct():
    assert tan(math.pi/4) == 1


def test_square_root_correct():
    assert square_root(49) == 7

def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-9)


def test_percentage_correct():
    assert percentage(25, 200) == 12.5


def test_percentage_whole_zero():
    with pytest.raises(ValueError):
        percentage(10, 0)