class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        # Returns a string with cookies represented by "🍪"
        return "🍪" * self.size

    def deposit(self, n):
        # Deposits a specified number of cookies into the jar
        if (self.size + n) > self.capacity:
            raise ValueError("Cookies exceeded capacity")
        self.size += n

    def withdraw(self, n):
        # Withdraws a specified number of cookies from the jar
        if (self.size - n) < 0:
            raise ValueError("There are not any cookies left in the cookie jar")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        # Sets the capacity of the jar, raising an exception for negative values
        if capacity < 0:
            raise ValueError("Capacity is negative int")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        # Sets the size of the jar (number of cookies), allowing direct manipulation
        self._size = size
