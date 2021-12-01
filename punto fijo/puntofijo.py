from math import sqrt
from prettytable import PrettyTable
from termcolor import colored

def f(x):
    return 4*x**2 + x**3 - 10

def g(x):
    return sqrt((10)/(x+4))

def fixed_point(x0, tol, n):
    Tabla = PrettyTable(
        ["iteración", colored("x", "red"), colored("g(x)", "magenta"), colored("f(x)", "yellow"), "error %"])

    for i in range(n):
        x = g(x0)
        if abs(x - x0) < tol:
            print(colored(f"La raiz es: {x} ", "green"))
            break

        error = round(abs(x - x0), 5)*100
        Tabla.add_row([i+1, round(x0, 4), round(g(x), 4),
                      round(f(x0), 5), round(error, 5)])
        x0 = x

    print(Tabla)

def main():
    fixed_point(x0=2, tol=0.00001, n=10)

if __name__ == "__main__":
    main()
