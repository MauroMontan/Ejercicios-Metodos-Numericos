from math import factorial


def maclaurin(x, n: int) -> dict:
    series = []
    result = 0
    sum = []
    for i in range(n):
        series.append((pow(x, i) / factorial(i)))
        result += series[i]
        sum.append(result)
    return series
