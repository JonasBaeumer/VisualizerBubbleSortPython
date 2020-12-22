from Code.bubblesort import bubble_sort
from Code.visualizer import Visualizer


def main():
    window = Visualizer("Bubble sort Visualizer", "1200x600")

    array = [1, 4, 7, 23, 5, 7, 1, 3]
    bubble_sort(array)


if __name__ == "__main__":
    main()


