class Person:
    def __init__(self, name, birthday, country) -> None:
        self.name = name
        self.birthday = birthday
        self.country = country


class Engineer(Person):
    def __init__(self, name, birthday, country, post) -> None:
        Person.__init__(self, name, birthday, country)
        self.post = post

    def greet(self):
        print(
            f"Engineer class with {self.name} {self.birthday} {self.country}")


class Pilot(Person):
    def __init__(self, name, birthday, country, post) -> None:
        Person.__init__(self, name, birthday, country)
        self.post = post

    def greet(self):
        print(f"pilot class with{self.name} {self.birthday} {self.country}")


class Vp(Engineer):
    def __init__(self, name, birthday, country, post) -> None:
        Engineer.__init__(self, name, birthday, country, post)
        print(f"Vp class with{self.name} {self.birthday} {self.country}")


Engineobj = Engineer('Celesty', '26/01/2001', 'India', 'CEO')
Engineobj.greet()
pilobj = Pilot('Celesty', '26/01/2001', 'India', 'Pilot')
pilobj.greet()
obj = Vp('Celesty', '26/01/2001', 'India', 'Vp')
obj.greet()
