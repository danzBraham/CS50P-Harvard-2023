from fuel import convert, gauge
import pytest


# Test a valid fraction
def test_valid_fraction():
    assert convert("3/4") == 75


# Test an invalid fraction where the numerator is greater than the denominator
def test_convert_invalid_fraction():
    with pytest.raises(ValueError):
        convert("5/2")


# Test a fraction with zero as the denominator
def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


# Test a non-integer fraction
def test_convert_non_integer_fraction():
    with pytest.raises(ValueError):
        convert("cat/4")


# Test an invalid input format that does not match "X/Y"
def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("3/4/5")


# Test a percentage value of 0 and 1
def test_gauge_less_than_or_equal_to_1():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


# Test a percentage value of 99 and 100
def test_gauge_greater_than_or_equal_to_99():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


# Test a percentage value of 50 and 75
def test_gauge_between_1_and_99():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
