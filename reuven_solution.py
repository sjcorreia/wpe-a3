#!/usr/bin/env python3

from collections import Counter
import typing


class NotEnoughSpaceError(Exception):
    pass


class Room():
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def __str__(self) -> str:
        return f'{self.name}, {self.size}m'


class House():
    def __init__(self, available_space: int = 100) -> None:
        self.rooms: typing.List[Room] = []
        self.available_space = available_space

    def add_rooms(self, *args: Room) -> None:
        for one_item in args:
            if self.size() + one_item.size > self.available_space:
                raise NotEnoughSpaceError(
                    f'{one_item.name} needs {one_item.size}; only {self.available_space - self.size()} available')
            self.rooms.append(one_item)

    def size(self) -> int:
        return sum(one_room.size
                   for one_room in self.rooms)

    def __str__(self) -> str:
        output = self.__class__.__name__ + ':\n'
        output += '\n'.join(str(one_room)
                            for one_room in self.rooms)
        return output

    def calculate_tax(self) -> float:
        return self.size() * 100


class SingleFamilyHouse(House):
    def __init__(self, available_space: int = 200) -> None:
        self.rooms: typing.List[Room] = []
        self.available_space = available_space

    def calculate_tax(self) -> float:
        s = self.size()
        if s <= 150:
            return s * 100 * 1.2
        else:
            return (150 * 100 * 1.2) + ((s - 150) * 100 * 1.5)


class TownHouse(House):
    def __init__(self, available_space: int = 100) -> None:
        self.rooms: typing.List[Room] = []
        self.available_space = available_space

    # no implementation of calculate_tax; we'll just use the inherited version


class Apartment(House):
    def __init__(self, available_space: int = 80) -> None:
        self.rooms: typing.List[Room] = []
        self.available_space = available_space

    def calculate_tax(self) -> float:
        return super().calculate_tax() * 0.75


class Neighborhood():
    total_size = 0

    def __init__(self) -> None:
        self.houses: typing.List[House] = []

    def add_houses(self, *args: House) -> None:
        for one_house in args:
            self.houses.append(one_house)
            Neighborhood.total_size += one_house.size()

    def size(self) -> int:
        return sum(one_house.size()
                   for one_house in self.houses)

    def house_types(self) -> typing.Counter[str]:
        return Counter(type(one_house).__name__
                       for one_house in self.houses)
