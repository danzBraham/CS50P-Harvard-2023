from twttr import shorten


# Test for a lowercase word containing vowels
def test_lowercase_word_with_vowels():
    assert shorten("twitter") == "twttr"


# Test for a lowercase word without vowels
def test_lowercase_word_without_vowels():
    assert shorten("myth") == "myth"


# Test for an uppercase word containing vowels
def test_uppercase_word_with_vowels():
    assert shorten("TWITTER") == "TWTTR"


# Test for an uppercase word without vowels
def test_uppercase_word_without_vowels():
    assert shorten("MYTH") == "MYTH"


# Test for a mixed-case word containing vowels
def test_mixed_case_word_with_vowels():
    assert shorten("TwItTeR") == "TwtTR"


# Test for a mixed-case word without vowels
def test_mixed_case_word_without_vowels():
    assert shorten("MyTh") == "MyTh"


# Test for a word with punctuation characters
def test_word_with_punctuation():
    assert shorten("twitt'er!?") == "twtt'r!?"


# Test for a word with numeric characters
def test_word_with_numbers():
    assert shorten("twitter07") == "twttr07"


# Test for an empty string
def test_empty_string():
    assert shorten("") == ""


# Test for a word consisting only of vowels
def test_word_with_only_vowels():
    assert shorten("aeiou") == ""
