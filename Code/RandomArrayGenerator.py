# this class is responsible for generating a random array with a set length
import random


def generate_random_array(length):
    array = []

    for i in range(length):
        array.append(random.randint(0, 100))
        # alternative: array += [random.randint(0, 100)]

    print(array)

    return array

