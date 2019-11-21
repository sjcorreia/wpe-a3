#!/usr/bin/env python
import json
from typing import Any, Dict


class ConfigFile( ):
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
                self.config[line.split(f"{self.sep}")[0]] = line.split(f"{self.sep}")[1].strip()
