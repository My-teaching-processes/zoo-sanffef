from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int, species: str) -> None:
        self._name = name
        self._age = age
        self._species = species
        self._energy = 50

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def energy(self) -> int:
        return self._energy

    @abstractmethod
    def make_sound(self) -> str:
        pass

    @abstractmethod
    def eat(self, food: str = "корм") -> None:
        pass

    def exercise(self, minutes: int) -> None:
        reduction = minutes // 2
        self._energy = max(0, self._energy - reduction)
        print(f"{self._name} тренировался. Энергия: {self._energy}")

    def sleep(self, hours: int) -> None:
        self._energy = min(100, self._energy + (hours * 15))
        print(f"{self._name} поспал. Энергия: {self._energy}")

    def get_info(self) -> str:
        return f"[{self._species}] {self._name}, Возраст: {self._age}, Энергия: {self._energy}"

    def __str__(self) -> str:
        return self.get_info()