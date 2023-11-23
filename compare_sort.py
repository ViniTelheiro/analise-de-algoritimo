import os
from tqdm import tqdm
import matplotlib.pyplot as plt

from utils import get_random_list, time_function
from SortMethods.buble_sort import BubleSort
from SortMethods.quick_sort import QuickSort


def compare_time() -> None:
    """This function compares the execution time between the two list sorted methods (BubleSort and QuickSort),
    whith differents lists size (10 to 10k whith step=20) and plot it into a graph.
    """
    save_path = "./result"
    if not os.path.isdir(save_path):
        os.makedirs(save_path)

    buble_sort_time = []
    quick_sort_time = []
    buble_sort = BubleSort()
    quick_sort = QuickSort()

    # get execution time in ms
    for i in tqdm(range(10, 9990 + 1, 20), total=len(range(10, 9990 + 1, 20))):
        shuffled_list = get_random_list(i)
    
        _, quick_time = time_function(f=quick_sort, input_list=shuffled_list.copy())
        _, buble_time = time_function(f=buble_sort, input_list=shuffled_list.copy())

        buble_sort_time.append(buble_time)
        quick_sort_time.append(quick_time)

    # Plotting the graph
    plt.plot(range(10, 9990 + 1, 20), buble_sort_time, c="b", label="Buble_sort")
    plt.plot(range(10, 9990 + 1, 20), quick_sort_time, c="r", label="Quick_sort")
    plt.xlabel("List_size")
    plt.ylabel("execution_time(s)")
    plt.title("BubleSort X QuickSort execution time (s) per list_size.")
    plt.legend()
    plt.savefig(os.path.join(save_path, "time_graph.jpeg"))
    plt.clf()


if __name__ == "__main__":
    compare_time()
