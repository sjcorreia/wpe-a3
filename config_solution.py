#!/usr/bin/env python
from typing import Any, Dict
from shutil import copy
import time


class ConfigFile:
    """This class will represent a configuration file"""

    def __init__(self, filename: str, sep: str = '=') -> None:
        self.filename = filename
        self.sep = sep
        self.config: Dict[str, str] = {}

    def set(self, key: str, value: Any) -> None:
        self.config[key] = str(value)

    def get(self, key: str) -> str:
        return self.config[key]

    def dump(self) -> None:
        """write to the file set in filename"""
        with open(self.filename, 'w') as file:
            for key, value in self.config.items():
                file.write(f"{key}{self.sep}{value}\n")

    def load(self) -> None:
        """read from filename"""
        with open(self.filename, 'r') as file:
            for line in file.readlines():
                key_value = line.split(f"{self.sep}")
                self.config[key_value[0]] = key_value[1].strip()


class ConfigFileWithBackups(ConfigFile):
    """"""

    def __init__(self, filename: str, sep: str = '=') -> None:
        super().__init__(filename, sep)

    def dump(self) -> None:
        """write to the file set in filename"""
        print(time.time())
        with open(self.filename, 'w') as file:
            for key, value in self.config.items():
                file.write(f"{key}{self.sep}{value}\n")
