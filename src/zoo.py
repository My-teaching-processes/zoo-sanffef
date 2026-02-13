from typing import List, Optional
from src.animal import Animal

class Zoo:
    def __init__(self, name: str, location: str) -> None:
        self._name = name
        self._location = location
        self._animals: List[Animal] = []

    @property
    def name(self) -> str: return self._name

    @property
    def location(self) -> str: return self._location

    @property
    def animals(self) -> List[Animal]:
        return self._animals[:]  # Возвращаем копию для теста

    def add_animal(self, animal: Animal) -> None:
        self._animals.append(animal)

    def remove_animal(self, animal: Animal) -> bool:
        if animal in self._animals:
            self._animals.remove(animal)
            return True
        return False

    def display_animals(self) -> None:
        print(f"\nЖивотные в {self._name}:")
        for animal in self._animals:
            print(f"- {animal}")

    def get_all_sounds(self) -> List[str]:
        return [animal.make_sound() for animal in self._animals]

    def feed_all(self) -> None:
        print("\n--- Кормление всех животных ---")
        for animal in self._animals:
            animal.eat()

    def exercise_all(self, minutes: int) -> None:
        for animal in self._animals:
            animal.exercise(minutes)

    def get_animal_count(self) -> int:
        return len(self._animals)

    def get_species_count(self, species_name: str) -> int:
        return sum(1 for a in self._animals if a.__class__.__name__ == species_name)

    def find_animal_by_name(self, name: str) -> Optional[Animal]:
        for animal in self._animals:
            if animal.name.lower() == name.lower():
                return animal
        return None

    def __str__(self) -> str:
        return f"Зоопарк '{self._name}' ({self._location})"