def add_doubled_values(my_list: list[int]):
    """
    Takes a list and adds the doubled values to the end
    [1,2,3] => [1,2,3,2,4,6]
    """
    my_list.update([x*2 for x in my_list])
