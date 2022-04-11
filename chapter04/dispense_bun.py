from typing import Optional


def are_buns_available():
    return

class Bun:
    def __init__(self) -> None:
        pass
    
    def add_frank(self, x):
        pass

def dispense_bun() -> Optional[Bun]:
    if not are_buns_available():
        return None
    return Bun()
