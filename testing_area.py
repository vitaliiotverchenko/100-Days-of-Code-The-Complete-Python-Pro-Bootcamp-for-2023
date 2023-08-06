class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

    def make_sound(self):
        print(f"{self.name} barks {self.sound}")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def make_sound(self):
        print(f"{self.name} meows {self.sound}")


# Створення об'єктів
dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")

# Виклик методів
dog1.make_sound()
cat1.make_sound()
