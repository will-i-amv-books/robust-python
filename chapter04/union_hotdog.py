from typing import Union, Optional


class HotDog:
    pass

class Pretzel:
    pass

def dispense_hot_dog(): return
def dispense_pretzel(): return
def print_error_code(): return
def get_order(): return

def dispense_snack(user_input: str) -> Union[HotDog, Pretzel]:
    if user_input == "Hot Dog":
        return dispense_hot_dog()
    elif user_input == "Pretzel":
        return dispense_pretzel()
    raise RuntimeError(
        "Should never reach this code, as an invalid input has been entered"
    )

def place_order() -> Optional[Union[HotDog, Pretzel]]:
    order = get_order()
    result = dispense_snack(order.name)
    if result is None:
        print_error_code("An error occurred" + result)
        return None
    return result # Return our HotDog