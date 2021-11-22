import os
from termcolor import colored
from maclaurin import maclaurin
from errors_calculator import percent_error, approximate_error
from table import init_table


# 1.648721
# x = 0.5

def main():
    iterator = 170
    expected_value = float(input("ingresa el valor de real: "))
    x = float(input("ingresa el valor de x: "))
    percent_errors = []
    expected_values = maclaurin(x, iterator)
    approximate_errors = []

    for given_value in maclaurin(x, iterator):
        percent_errors.append(percent_error(given_value, expected_value))

    for index in range(len(expected_values)):
        approximate_errors.append(approximate_error(
            expected_values[index], expected_values[index-1]))

    if approximate_errors[-1] >= percent_errors[-1]:
        init_table(iterator, expected_values,
                   percent_errors, approximate_errors)
        print(colored("no se ha aproximado todo lo que puede", "red"))

    if approximate_errors[-1] <= percent_errors[-1]:
        if approximate_errors[-1] == 0.0:
            final_lenght = list(dict.fromkeys(approximate_errors))
            init_table(len(final_lenght), expected_values,
                       percent_errors, approximate_errors)

        print(colored(
            f"se tomaron {len(final_lenght)-1} iteraciones!, el valor del error mas aproximado es: {final_lenght[-2]}", "blue"))


if __name__ == '__main__':
    main()
    
    os.system("PAUSE")
