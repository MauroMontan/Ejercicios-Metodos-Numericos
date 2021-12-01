from math import *
from prettytable import PrettyTable
from termcolor import colored


def f(x: float, fn: str) -> float:
    return eval(fn)


def percent_error(x: float, x_old: float) -> float:
    return abs((x - x_old)/x)*100


def bisection(a: float, b: float, tol: float, fn: str) -> None:
    x_old: int = 0
    x: float = (a + b)/2
    i: int = 0
    Table = PrettyTable(
        ["Iteraciones", "Valor aproximado", "Error Porcentual %", "Error aproximado"])

    while percent_error(x, x_old) > tol:
        x_old = x
        if f(x, fn) == 0:
            print(f"La raiz es: {x} ")
        elif f(a, fn)*f(x, fn) < 0:
            b = x
        else:
            a = x

        x = round((a + b)/2, 4)
        i += 1
        Table.add_row([i, x, round(percent_error(x, x_old), 3),
                      round(abs(x - x_old), 3)])
    print(Table)
    print(colored(f"La raiz es: {x} \n".center(70), "green"))


def main() -> None:
    print(colored("Encuentra las raices de una función", "blue"))
    fn = input(colored("Ingrese una función: ", "yellow"))
    print(colored("Ingrese el intervalo [a,b]", "magenta"))
    lim_inf = float(input(colored("Ingrese el limite inferior: ", "yellow")))
    lim_sup = float(input(colored("Ingrese el limite superior: ", "yellow")))
    tol = float(input(colored("Ingrese la tolerancia: ", "yellow")))

    # EStos SON LOS DATOS DEl ejercicio
    #function = x**4 + 3*x**3 - 2
    #lim_inf = 0
    #lim_sup = 1
    #tol = 0.0001

    bisection(lim_inf, lim_sup, tol, fn=fn)


if __name__ == "__main__":
    main()
