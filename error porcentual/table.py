from prettytable import PrettyTable
from termcolor import colored


def init_table(iterator, expected_values, percent_errors, approximate_errors):
    Table = PrettyTable(["Iteraciones", "Valor aproximado",
                        "Error Porcentual %", "Error aproximado"])

    for i in range(iterator):
        Table.add_row([i+1, colored(f"{expected_values[i]}", "blue"),
                      colored(f"{percent_errors[i]} %", "yellow"), colored(f"{approximate_errors[i]}", "green")])

    print(Table)
