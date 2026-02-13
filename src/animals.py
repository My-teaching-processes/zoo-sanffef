from typing import Optional
from src.animal import Animal

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age, "Dog")
        self._breed = breed
        self._tricks = []

    @property
    def breed(self) -> str:
        return self._breed

    def make_sound(self) -> str:
        return f"{self._name} says: Woof! Woof!"

    def eat(self, food: str = "мясо") -> None:
        self._energy = min(100, self._energy + 20)
        print(f"{self._name} съел {food}!")

    def teach_trick(self, trick: str) -> None:
        if trick not in self._tricks:
            self._tricks.append(trick)

    def perform_trick(self, trick: str) -> str:
        if trick in self._tricks:
            self._energy = max(0, self._energy - 10)
            return f"{self._name} performed the trick: {trick}!"
        return f"{self._name} hasn't learned the {trick} trick yet."

class Cat(Animal):
    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(name, age, "Cat")
        self._color = color

    def make_sound(self) -> str:
        return f"{self._name} says: Meow!"

    def eat(self, food: str = "рыбу") -> None:
        self._energy = min(100, self._energy + 15)
        print(f"{self._name} съел {food}!")

    def scratch(self, target: str = "furniture") -> str:
        return f"{self._name} is scratching the {target}!"

class Bird(Animal):
    def __init__(self, name: str, age: int, species: str, can_fly: bool = True) -> None:
        super().__init__(name, age, "Bird")
        self._bird_species = species
        self._can_fly = can_fly
        self._altitude = 0

    @property
    def altitude(self) -> int:
        return self._altitude

    def make_sound(self) -> str:
        return f"{self._name} says: Tweet! Tweet!"

    def eat(self, food: str = "зерно") -> None:
        self._energy = min(100, self._energy + 10)

    def fly(self, altitude: int) -> str:
        if not self._can_fly:
            return f"{self._name} cannot fly."
        self._altitude = altitude
        self._energy = max(0, self._energy - 20)
        return f"{self._name} flew to {altitude} meters!"

    def land(self) -> str:
        self._altitude = 0
        return f"{self._name} has landed!"
        return f"{self._name} has landed."