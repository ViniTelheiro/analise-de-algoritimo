from typing import Any


class BubleSort:
    """This class is the implementation of the BubleSort method in lists
    """
    def __init__(self) -> None:
        pass

    def _move_backward(self, input_list: list[int], idx: int) -> None:
        input_list.insert(idx, input_list[idx + 1])
        input_list.pop(idx + 2)
        self.swap = True

    def __call__(self, input_list: list[int]) -> list[int]:
        """Use the call method to sort a input list.

        Args:
            input_list (list[int]): List to be sorted

        Returns:
            list[int]: sorted list
        """
        while True:
            self.swap = False
            [
                self._move_backward(input_list=input_list, idx=idx)
                for idx in range(len(input_list) - 1)
                if input_list[idx] > input_list[idx + 1]
            ]
            if self.swap == False:
                break
        return input_list
