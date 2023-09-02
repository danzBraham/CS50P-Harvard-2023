import pytest
from working import convert


# Test conversion from AM/PM format (8 AM to 5 PM) to 24-hour format
def test_am_pm_format_8am_to_5pm():
    assert convert("8 AM to 5 PM") == "08:00 to 17:00"


# Test conversion from AM/PM format (9:00 AM to 6:00 PM) to 24-hour format
def test_am_pm_format_9am_to_6pm():
    assert convert("9:00 AM to 6:00 PM") == "09:00 to 18:00"


# Test conversion from AM/PM format (10:30 AM to 5 PM) to 24-hour format
def test_am_pm_format_1030am_to_5pm():
    assert convert("10:30 AM to 5 PM") == "10:30 to 17:00"


# Test conversion from AM/PM format (11 AM to 5:30 PM) to 24-hour format
def test_am_pm_format_11am_to_530pm():
    assert convert("11 AM to 5:30 PM") == "11:00 to 17:30"


# Test conversion from PM/AM format (5 PM to 3 AM) to 24-hour format
def test_pm_am_format_5pm_to_3am():
    assert convert("5 PM to 3 AM") == "17:00 to 03:00"


# Test conversion from PM/AM format (6:00 PM to 4:00 AM) to 24-hour format
def test_pm_am_format_6pm_to_4am():
    assert convert("6:00 PM to 4:00 AM") == "18:00 to 04:00"


# Test conversion from PM/AM format (7:30 PM to 4 AM) to 24-hour format
def test_pm_am_format_730pm_to_4am():
    assert convert("7:30 PM to 4 AM") == "19:30 to 04:00"


# Test conversion from PM/AM format (8 PM to 4:45 AM) to 24-hour format
def test_pm_am_format_8pm_to_445am():
    assert convert("8 PM to 4:45 AM") == "20:00 to 04:45"


# Test conversion with invalid time input (9:60 AM to 5:60 PM)
def test_invalid_time_960am_to_560pm():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


# Test conversion with invalid time input (7 AM - 5 PM)
def test_invalid_time_7am_to_5pm_dash():
    with pytest.raises(ValueError):
        convert("7 AM - 5 PM")


# Test conversion with invalid time input (8:00 AM - 6:00 PM)
def test_invalid_time_800am_to_600pm_dash():
    with pytest.raises(ValueError):
        convert("8:00 AM - 6:00 PM")
