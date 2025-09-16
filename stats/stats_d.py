from discrete import *
from tabulate import tabulate

def main(): # ========== FOR DISCRETE SERIES ==========
    x = []
    f = []
    N = 0
    fx = []
    Efx = 0

    data = []
    header = ["x", "f", "fx"]

    print()

    x = store_values_to_x(x)
    f = store_values_to_f(f)
    N = calculate_N(f)

    for i in range(len(x)):
        for_fx = 0
        for_fx = int(x[i]) * int(f[i])
        fx.append(for_fx)

    for i in fx:
        Efx += i

    mean = Efx / N

    print()

    for i in range(len(x)):
        data.append([int(x[i]), int(f[i]), int(fx[i])])

    print(tabulate(data, headers=header, tablefmt="simple_grid"))

    print(f"\nN = {N}\nEfx = {Efx}\nMean = {float(mean):.2f}")


if __name__ == "__main__":
    main()