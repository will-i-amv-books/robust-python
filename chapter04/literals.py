from typing import Literal
from dataclasses import dataclass


@dataclass
class Error:
    error_code: Literal[1, 2 ,3, 4, 5]
    disposed_of: bool


@dataclass
class Snack:
    name: Literal["Pretzel", "Hot Dog", "Veggie Burger"]
    condiments: set[Literal["Mustard", "Ketchup"]]


Error(0, False)
Snack("Invalid", set())
Snack("Pretzel", {"Mustard", "Relish"})
