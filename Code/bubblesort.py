# This class is responsible for implementing and executing the bubblesort algorithm
# on a given array of numbers (integers)

def bubble_sort(array):

    if array is None:
        print("Try again.")

    for j in range(len(array), 0, -1):

        # Walk through the array from left to right
        for i in range(len(array)-1):

            # Compare the current element with the next right one
            if array[i] > array[i+1]:
                #packing and unpacking
                array[i], array[i+1] = array[i+1], array[i]
