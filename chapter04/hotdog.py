from dispense_bun import dispense_bun


def dispense_frank(): return
def dispense_mustard(): return
def dispense_ketchup(): return
def dispense_hot_dog_to_customer(x): return
def print_error_code(x): return


def create_hot_dog() -> None:
    bun = dispense_bun()
    if bun is None:
        print_error_code("Bun could not be dispensed")
        return

    frank = dispense_frank()
    hot_dog = bun.add_frank(frank)
    ketchup = dispense_frank()
    mustard = dispense_mustard()
    hot_dog.add_condiments(ketchup, mustard)
    dispense_hot_dog_to_customer(hot_dog)
