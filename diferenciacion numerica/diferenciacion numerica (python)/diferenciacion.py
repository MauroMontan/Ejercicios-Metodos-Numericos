# f(x) = -0.1*x**4 - 0.15*x**3 - 0.5*x**2 -0.25*x + 1.2
# f'(x) = -0.4*x**3 - 0.45*x**2 - 1*x - 0.25
# valor de h = 0.5
# valor de x = 0.5
# para adelante x + h
# para atras x - h
# para central x

def f(x) -> float:
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2


def f_prime(x) -> float:
    return -0.4*x**3 - 0.45*x**2 - 1*x - 0.25


def forward_diff(x: float, h: float) -> float:
    return (f(x+h) - f(x))/h


def backward_diff(x: float, h: float) -> float:
    return (f(x)-f(x-h))/h


def cetral_diff(x: float, h: float) -> float:
    return (f(x+h)-f(x-h))/(2*h)


def error(x: float, h: float, function):
    return abs((f_prime(x) - function)/f_prime(x)*100)


def method(type: str, x: float, h: float, function):
    print(f"aproximacion: {type}")
    print(f"f'({x}): {function(x,h)}")
    print(f"error porcentual:{error(x,h,function(x,h))} %")


def main():
    x: float = 0.5
    h: float = 0.5

    method("Hacia delante", x, h, forward_diff)
    method("Hacia atras", x, h, backward_diff)
    method("Centrada", x, h, cetral_diff)

    print(f"valor real: {f_prime(x)} ")


if __name__ == "__main__":
    main()
