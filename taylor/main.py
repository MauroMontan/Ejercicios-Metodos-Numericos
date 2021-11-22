from taylor import Taylor
from prettytable import PrettyTable
#  
# function = "-0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2"
# function_prueba = -0.5*x**2 -0.3*x + 0.9
# h = 1
# xi = 0


def main():
    function = input("Ingresa una Función: ")
    iterator = int(input("Ingresa el numero de terminos: "))
    xi = float(input("Ingresa el valor de xi: "))
    h = float(input("Ingresa el valor de h: "))

    taylor_serie = Taylor(function=function, var=xi, iterator=iterator)

    Table = PrettyTable(["n", "derivada", "Valor de la derivada",
                        "termino", "suma", "Err. de truncamiento"])

    for i in range(iterator):
        Table.add_row([i, taylor_serie.symbolic_derivative()[i],
                       round(taylor_serie.numeric_derivative(h)[i], 3),
                       round(taylor_serie.taylor(
                           iterator, h)["terminos"][i], 4),
                       taylor_serie.taylor(iterator, h)["Sumas"][i],
                       round(taylor_serie.taylor(iterator, h)["errores"][i], 4)])

    print(Table)

    print(f"valor a predecir: {round(taylor_serie.true_value,4)}")
    print(f" suma total de la serie: {taylor_serie.taylor(iterator,h)['Suma total']}")


if __name__ == '__main__':
    main()
