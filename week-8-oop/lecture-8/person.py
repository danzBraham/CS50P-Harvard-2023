class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


class Student(Person):
    def __init__(self, name, city):
        super().__init__(name)
        self.city = city

    def __str__(self):
        return f"{self.name} is from {self.city}"

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if city not in ["London", "Birmingham", "Manchester"]:
            raise ValueError("Invalid city")
        self._city = city


class Parent(Person):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job

    def __str__(self):
        return f"{self.name}'s job is a {self.job}"

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        self._job = job


def main():
    person = Person("John")
    student = Student("Abra", "Manchester")
    parent = Parent("Danzi", "Programmer")

    print(person)
    print(student)
    print(parent)


if __name__ == "__main__":
    main()
