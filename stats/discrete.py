def store_values_to_x(array):
    values = input("Enter the value of x (space-separated): ")

    for i in values.split(" "):
        array.append(i)

    return array


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