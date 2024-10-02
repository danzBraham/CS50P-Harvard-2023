class Developer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.capitalize().strip()


class Student(Developer):
    def __init__(self, name, city):
        super().__init__(name)
        self.city = city

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if not city:
            raise ValueError("Missing city")
        self._city = city.capitalize().strip()


class Mentor(Developer):
    def __init__(self, name, expertise):
        super().__init__(name)
        self.expertise = expertise

    @property
    def expertise(self):
        return self._expertise

    @expertise.setter
    def expertise(self, expertise):
        if not expertise:
            raise ValueError("Missing expertise")
        self._expertise = expertise.capitalize().strip()


def main():
    developer = Developer("zidan")
    student = Student("abra", "denpasar")
    mentor = Mentor("indra", "full-stack")

    print(f"{developer.name} is a developer")
    print(f"{student.name} is a student from {student.city}")
    print(f"{mentor.name} is a mentor expertise in {mentor.expertise}")


if __name__ == "__main__":
    main()
