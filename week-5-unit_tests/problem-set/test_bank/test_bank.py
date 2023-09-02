from bank import value


# Test for a greeting that starts with "hello"
def test_greeting_starts_with_hello():
    assert value("hello, how are you?") == 0


# Test for a greeting that starts with "Hello" (case-insensitive)
def test_greeting_starts_with_hello_case_insensitive():
    assert value("Hello, how are you?") == 0


# Test for a greeting that starts with "h"
def test_greeting_starts_with_h():
    assert value("hey") == 20


# Test for a greeting that starts with "H" (case-insensitive)
def test_greeting_starts_with_h_case_insensitive():
    assert value("How's it going?") == 20


# Test for a greeting that doesn't start with "hello" or "h"
def test_greeting_starts_without_h():
    assert value("what's up") == 100


# Test for an empty string as the greeting
def test_greeting_empty_string():
    assert value("") == 100


# Test for a greeting consisting of whitespace characters only
def test_greeting_whitespace_only():
    assert value("    ") == 100
