from numb3rs import validate


# Test with 1 digit in each octet
def test_one_digit_in_ipv4():
    assert validate("1.1.1.1") == True


# Test with 2 digits in each octet
def test_two_digits_in_ipv4():
    assert validate("71.72.73.74") == True


# Test with 3 digits in each octet
def test_three_digits_in_ipv4():
    assert validate("171.172.173.174") == True


# Test with 4 digits in each octet
def test_four_digits_in_ipv4():
    assert validate("1712.1723.1734.1745") == False


# Test with 1 digit and 2 digits in octets
def test_one_and_two_digits_in_ipv4():
    assert validate("1.17.18.14") == True


# Test with 2 digits and 3 digits in octets
def test_two_and_three_digits_in_ipv4():
    assert validate("17.172.173.174") == True


# Test with 3 digits and 4 digits in octets
def test_three_and_four_digits_in_ipv4():
    assert validate("1737.172.1736.1747") == False


# Test with a word instead of an IPv4 address
def test_word_in_ipv4():
    assert validate("cat") == False


# Test with multiple words instead of an IPv4 address
def test_words_in_ipv4():
    assert validate("cat.dog.fish.bird") == False


# Test case for an IPv4 address with the first byte outside the range 0-255
def test_first_byte_out_of_range():
    assert validate("277.7.0.1") == False


# Test case for an IPv4 address with the second byte outside the range 0-255
def test_second_byte_out_of_range():
    assert validate("75.456.76.65") == False


# Test case for an IPv4 address with the third byte outside the range 0-255 with minus digit
def test_third_byte_out_of_range_with_minus_digit():
    assert validate("51.0.-1.1") == False


# Test case for an IPv4 address with the fourth byte outside the range 0-255 with word
def test_fourth_byte_out_of_range_with_words():
    assert validate("1.0.0.cat") == False


# Test case for an invalid IPv4 address with missing octets
def test_ip_address_with_three_octets():
    assert validate("192.168.0") == False


# Test case for an invalid IPv4 address with additional octets
def test_ip_address_with_five_octets():
    assert validate("10.0.0.1.2") == False


# Test case for an IPv4 address with zero
def test_zero():
    assert validate("0.0.0.0") == True
