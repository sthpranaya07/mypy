def store_values_to_CI(array):
    values = input("Enter the class intervals (space-separated): ")

    for i in values.split(" "):
        array.append(i)

    return array


def store_values_to_m(array1, array2):
    for class_intervals in array1:
        bounds = class_intervals.split("-")
        lower = int(bounds[0])
        upper = int(bounds[1])
        midpoint = (lower + upper) / 2
        array2.append(int(midpoint))

    return array2


def store_values_to_f(array):
    values = input("Enter the value of f (space-separated): ")

    for i in values.split(" "):
        array.append(i)

    return array


def calculate_N(array):
    N = 0
    for frequencies in array:
        N += int(frequencies)

    return N