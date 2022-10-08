
# Sets Jar class
class Jar:
    # Jar instance with and raise value error is the capacity is non-integer
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self.cookie_jar = []

    # Returns the number of cookies in the cookie_jar
    def __str__(self):
        return self.size * "🍪"

    # Adds cookies to the cookie_jar or raise error if it exceeds the capacity
    def deposit(self, n):
        for _ in range(n):
            self.cookie_jar.append("🍪")
        if self.size > self.capacity:
            raise ValueError
    # Removes cookies from cookie_jar or raise error if there aren't that many cookies
    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        for _ in range(n):
            self.cookie_jar.pop()


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return len(self.cookie_jar)


# New instance of jar to test 
jar = Jar()

jar.deposit(6)
print(jar)
jar.withdraw(3)
print(jar)
