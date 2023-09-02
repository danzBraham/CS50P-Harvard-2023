import pytest
from jar import Jar


# Test initialization of Jar object
def test_init():
    jar = Jar()
    assert jar.capacity == 12


# Test empty string representation of Jar object
def test_empty_str():
    jar = Jar(10)
    assert str(jar) == ""  # Empty jar


# Test string representation of Jar object
def test_str():
    jar = Jar(10)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"  # Jar with 3 cookies
    jar.deposit(7)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"  # Jar with 10 cookies


# Test depositing cookies into the jar
def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    jar.deposit(5)
    assert jar.size == 8  # Total size of the jar after deposits


# Test withdrawing cookies from the jar
def test_withdraw():
    jar = Jar(10)
    jar.deposit(9)
    jar.withdraw(6)
    assert jar.size == 3  # Total size of the jar after withdrawals


# Test creating a Jar object with a negative capacity
def test_capacity_negative():
    with pytest.raises(ValueError):
        Jar(-5)


# Test depositing cookies that exceed the capacity of the jar
def test_capacity_exceeded():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(20)
