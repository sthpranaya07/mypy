from continuos import *
from tabulate import tabulate

def main(): # ========== FOR CONTINUOUS SERIES ==========
    CI = []
    f = []
    m = []
    N = 0
    fm = []
    Efm = 0

    data = []
    header = ["CF", "f", "m", "fm"]

    print()

    CI = store_values_to_CI(CI)
    f = store_values_to_f(f)
    m = store_values_to_m(CI, m)
    N = calculate_N(f)

    for i in range(len(CI)):
        for_fm = 0
        for_fm += int(f[i]) * int(m[i])
        fm.append(for_fm)

    for i in fm:
        Efm += i

    mean = Efm / N

    print()

    for i in range(len(CI)):
        data.append([CI[i], int(f[i]), int(m[i]), int(fm[i])])

    print(tabulate(data, headers=header, tablefmt="simple_grid"))

    print(f"\nN = {N}\nEfm = {Efm}\nMean = {float(mean):.2f}")


if __name__ == "__main__":
    main()