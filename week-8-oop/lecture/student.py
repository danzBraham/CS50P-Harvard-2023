class Student:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @classmethod
    def get(cls):
        name = input("Name: ").capitalize().strip()
        city = input("City: ").capitalize().strip()
        return cls(name, city)

    def greetings(self):
        return f"Hello i am {self.name}!"

    def __str__(self):
        return f"{self.name} from {self.city}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name.capitalize()

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if not city:
            raise ValueError("Missing city")
        self._city = city.capitalize()


def main():
    student = Student.get()
    print(student.name)
    print(student.city)


if __name__ == "__main__":
    main()
