from plates import is_valid


# Test for a plate with length less than 2
def test_plate_length_less_than_two():
    assert is_valid("A") == False


# Test for a plate with length greater than 6
def test_plate_length_greater_than_six():
    assert is_valid("AAAA765") == False


# Test for a plate with mixed non-alphanumeric characters
def test_plate_with_mixed_non_alphanumeric():
    assert is_valid("AA?765") == False


# Test for a plate with mixed alphanumeric characters
def test_plate_with_mixed_alphanumeric():
    assert is_valid("ABCD12") == True


# Test for a plate with alphabetic characters only
def test_plate_with_alpha_only():
    assert is_valid("XYZ") == True


# Test for a plate with zeros in the middle
def test_plate_with_zeros():
    assert is_valid("AAA000") == False


# Test for a plate with leading zeros
def test_plate_with_leading_zeros():
    assert is_valid("AAA070") == False


# Test for a plate with a number in the first position
def test_plate_with_number_in_first_position():
    assert is_valid("1AAAAA") == False


# Test for a plate with a number in the middle
def test_plate_with_number_in_middle():
    assert is_valid("A1AAAA") == False


# Test for a plate number placed in both first and last positions
def test_plate_with_number_in_first_and_last_position():
    assert is_valid("1AA1A2") == False


# Test for a plate number placed in both middle and last positions
def test_plate_with_number_in_middle_and_last_position():
    assert is_valid("AA1A23") == False


# Test for a plate number placed in both middle and first positions
def test_plate_with_number_in_middle_and_first_position():
    assert is_valid("1A12AC") == False


# Test for a plate with a non-zero number in the middle to the end
def test_plate_with_non_zero_number_in_middle_to_end():
    assert is_valid("AAA700") == True


# Test for a plate with numeric characters only
def test_plate_with_numeric_only():
    assert is_valid("123456") == False
