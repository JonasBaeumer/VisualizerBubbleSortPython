# This class is responsible for implementing and executing the bubblesort algorithm
# on a given array of numbers (integers)

def bubblesort(array):

    if array is None:
        print("Du kleiner Schlingel, versuch es nochmal.")

    j = len(array)

    while j > 1:

        i = 0

        # Das Array wird von links nach rechts durchlaufen
        while i < len(array) - 1:

            valueNow = array[i]
            valueRight = array[i + 1]

            if valueNow > valueRight:
                valueswap(valueNow, valueRight, array, i)

            i += 1

        j -= 1


def valueswap(valueNow, valueRight, array, position):
    array[position + 1] = valueNow
    array[position] = valueRight

    # Bei jedem Schritt vergleiche das aktuelle Element mit seinem Nachbarn

    # Ist das aktuelle Element kleiner als das rechte, werden die Elemente vertauscht
