#!/usr/bin/env python
from collections import Counter
from typing import List, Dict


class NotEnoughSpaceError(Exception):
    """Raised when the House does not have enough space for
    additional rooms"""
    pass


class ConfigFile():
    """This class to model a room, including name and size"""

    def __init__(self) -> None:
        pass

    def set(self) -> None:
        pass

    def get(self) -> None:
        pass

    def dump(self) -> None:
        pass

    def load(self) -> None:
        pass
