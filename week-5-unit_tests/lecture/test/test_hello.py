from hello import greet


def test_default():
    assert greet() == "hello world"


def test_argument():
    assert greet("john") == "hello john"
