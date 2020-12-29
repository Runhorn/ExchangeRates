from enum import Enum


class MyException(Exception):
    def __init__(self, name: str):
        self.name = name


class Currencies(str, Enum):
    usd = "usd"
    eur = "eur"
    chf = "chf"
    gbp = "gbp"

