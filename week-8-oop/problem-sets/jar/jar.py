class Jar:
    def __init__(self, capacity=12):
        # Initialize the jar with default capacity (12) and set the initial size to 0
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        # Return a string of 🍪 representing the number of cookies in the jar (size)
        return "🍪" * self.size

    def deposit(self, n):
        # Add `n` cookies to the jar, raise error if it exceeds capacity
        if self.size + n > self.capacity:
            raise ValueError(
                f"Cannot deposit {n} cookies. Exceeds jar capacity of {self.capacity}."
            )
        self.size += n

    def withdraw(self, n):
        # Remove `n` cookies from the jar, raise error if there aren't enough cookies
        if n > self.size:
            raise ValueError(
                f"Cannot withdraw {n} cookies. Only {self.size} cookies available in the jar."
            )
        self.size -= n

    @property
    def capacity(self):
        # Return the current capacity of the jar
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        # Set the jar's capacity, raise error if it's negative
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")
        self._capacity = capacity

    @property
    def size(self):
        # Return the current size (number of cookies) in the jar
        return self._size

    @size.setter
    def size(self, size):
        # Set the jar's size, raise error if it's negative
        if size < 0:
            raise ValueError("Size cannot be negative.")
        self._size = size
