from random import randint
from time import time


def get_random_list(list_size: int) -> list[int]:
    """This function generates a shuffled list with random numbers between 1 and 1000

    Args:
        list_size (int): The size of the list

    Raises:
        ValueError: The list_size must be an integer value
        ValueError: The list_size must be < 1

    Returns:
        list[int]: The shuffled list.
    """
    if not isinstance(list_size, int):
        raise ValueError("The list_size must be an integer value.")
    if list_size < 1:
        raise ValueError("The list_size must be bigger than one")
    rl = []
    [rl.append(randint(1, 1000)) for i in range(list_size)]
    return rl


def time_function(f: callable, **kwargs) -> list[any, float]:
    """This function calculate the execution time (in seconds) of an callable

    Args:
        f (callable): The callable that the time will be calculated.

    Returns:
        list[any, float]: A list with the callable output and the execution time in secounds
    """
    t0 = time()
    otp = f(**kwargs)
    return [otp, (time() - t0)]
