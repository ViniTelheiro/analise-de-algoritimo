class QuickSort:
    """This class implementates the QuickSort method in a list."""

    def __init__(self) -> None:
        pass

    def __call__(self, input_list: list[int]) -> list[int]:
        """Use the call method to sort a list.

        Args:
            input_list (list[int]): input list to be sorted

        Returns:
            list[int]: Sorted list.
        """
        ord_list = []
        pivot = input_list[-1]
        input_list.remove(pivot)

        lower = list(filter(lambda x: x <= pivot, input_list))
        if len(lower) > 0:
            ord_list.append(lower[:])

        ord_list.append([pivot])

        bigger = list(filter(lambda x: x > pivot, input_list))
        if len(bigger) > 0:
            ord_list.append(bigger[:])

        while True:
            last = True
            ord_temp_list = []
            for i in range(len(ord_list)):
                if len(ord_list[i]) == 1:
                    ord_temp_list.append(ord_list[i])
                    continue

                temp_list = ord_list[i].copy()

                pivot = temp_list[-1]
                temp_list.remove(pivot)

                lower = list(filter(lambda x: x <= pivot, temp_list))
                if len(lower) > 0:
                    ord_temp_list.append(lower[:])

                ord_temp_list.append([pivot])

                bigger = list(filter(lambda x: x > pivot, temp_list))
                if len(bigger) > 0:
                    ord_temp_list.append(bigger[:])

                last = False

            ord_list = ord_temp_list.copy()

            if last:
                break

        output = []
        [[output.append(j) for j in i] for i in ord_list]
        return output
