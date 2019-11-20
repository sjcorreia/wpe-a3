#!/usr/bin/env python
from collections import Counter
from typing import List, Dict


class NotEnoughSpaceError(Exception):
    """Raised when the House does not have enough space for
    additional rooms"""
    pass


class Room:
    """This class to model a room, including name and size"""

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def __str__(self) -> str:
        return "{self.name}, {self.size}m".format(self=self)


class House:
    """Class to model house, with rooms of various sizes"""

    def __init__(self, available_space: int = 100,
                 house_size: int = 0, rooms: List[Room] = []) -> None:
        self.available_space = available_space
        self._house_size = house_size
        if not rooms:
            rooms = []
        self.rooms: List[Room] = rooms

    def __str__(self) -> str:
        house_output = ""
        for room in self.rooms:
            house_output += "\n" + str(room)
        return "{}:{}".format(self.__class__.__name__, house_output)

    def __add__(self, other: Room) -> 'House':
        self.add_rooms(other)
        return self

    def size(self) -> int:
        return self._house_size

    def add_rooms(self, *rooms: Room) -> None:
        for room in rooms:
            if self.available_space >= self._house_size + room.size:
                self._house_size += room.size
                self.rooms.append(room)
            else:
                raise NotEnoughSpaceError

    def calculate_tax(self) -> float:
        return self._house_size * 100.0


class Neighborhood:
    """Class to model a neighborhood, including several houses"""

    total_size = 0

    def __init__(self, name: str = '') -> None:
        self._name = name
        self.houses: List[House] = []

    def __add__(self, other: House) -> 'Neighborhood':
        self.add_houses(other)
        return self

    def size(self) -> int:
        return sum(house.size() for house in self.houses)

    def add_houses(self, *houses: House) -> None:
        for house in houses:
            self.houses.append(house)
            Neighborhood.total_size += house.size()

    def house_types(self) -> Dict[str, int]:
        counter: Dict[str, int] = Counter()
        for house in self.houses:
            counter[house.__class__.__name__] += 1
        return counter

    def calculate_tax(self) -> float:
        return sum(house.calculate_tax() for house in self.houses)

    def find_with_room(self, **kwargs) -> set:
        obj = vars(kwargs)
        print(obj)
        return set()


class Apartment(House):
    """"house type with default space 80"""

    def __init__(self, available_space: int = 80) -> None:
        super().__init__(available_space)

    def calculate_tax(self) -> float:
        return self._house_size * 100 * 0.75


class TownHouse(House):
    """"house type with default space 100"""

    def __init__(self, available_space: int = 100) -> None:
        super().__init__(available_space)


class SingleFamilyHouse(House):
    """"house type with default space 200"""

    def __init__(self, available_space: int = 200) -> None:
        super().__init__(available_space)

    def calculate_tax(self) -> float:
        if self._house_size > 150:
            total_tax = (150*100*1.2) + ((self._house_size - 150)*100*1.5)
        else:
            total_tax = self._house_size * 100 * 1.2
        return total_tax
