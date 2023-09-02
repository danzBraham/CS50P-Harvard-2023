from datetime import date, timedelta
import pytest
from seasons import calculate_age_in_minutes


# Test case when no input is provided
def test_without_input():
    with pytest.raises(SystemExit):
        calculate_age_in_minutes("") == "Invalid Date"


# Test case for an invalid date format
def test_invalid_date():
    with pytest.raises(SystemExit):
        calculate_age_in_minutes("January 1, 2020") == "Invalid Date"


# Test case for one year age
def test_one_year():
    d = str(date.today() - timedelta(days=365))
    assert (
        calculate_age_in_minutes(d)
        == "Five hundred twenty-five thousand, six hundred minutes"
    )


# Test case for five years age
def test_five_years():
    d = str(date.today() - timedelta(days=365 * 5))
    assert (
        calculate_age_in_minutes(d)
        == "Two million, six hundred twenty-eight thousand minutes"
    )


# Test case for ten years age
def test_ten_years():
    d = str(date.today() - timedelta(days=365 * 10))
    assert (
        calculate_age_in_minutes(d)
        == "Five million, two hundred fifty-six thousand minutes"
    )


# Test case for twenty years age
def test_twenty_years():
    d = str(date.today() - timedelta(days=365 * 20))
    assert (
        calculate_age_in_minutes(d)
        == "Ten million, five hundred twelve thousand minutes"
    )
