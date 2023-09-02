class Student:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return f"{self.name} from {self.city}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if city not in ["London", "Birmingham", "Manchester", "Paris"]:
            raise ValueError("Invalid city")
        self._city = city

    @classmethod
    def get(cls):
        name = input("Name: ")
        city = input("City: ")
        return cls(name, city)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
