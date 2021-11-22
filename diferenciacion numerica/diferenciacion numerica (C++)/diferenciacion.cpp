#include <iostream>
#include <cmath>
using namespace std;

//f(x) = -0.1*x**4 - 0.15*x**3 - 0.5*x**2 -0.25*x + 1.2
//f'(x) = -0.4*x**3 - 0.45*x**2 - 1*x - 0.25
//valor de h = 0.5
//valor de x = 0.5

double f(double x)
{
    return -0.1 * (pow(x, 4)) - 0.15 * (pow(x, 3)) - 0.5 * (pow(x, 2)) - 0.25 * x + 1.2;
}

double f_prime(double x)
{
    return -0.4 * (pow(x, 3)) - 0.45 * (pow(x, 2)) - 1 * x - 0.25;
}

double central_diff(float x, float h)
{
    return (f(x + h) - f(x - h)) / (2 * h);
}

double forward_diff(float x, float h)
{
    return (f(x + h) - f(x)) / h;
}

double backward_diff(float x, float h)
{
    return (f(x) - f(x - h)) / h;
}

double error(float x, float h, double function)
{
    return abs((f_prime(x) - function) / f_prime(x) * 100);
}

void method(string type, float x, float h, double function)
{
    cout << "\n"
         << type << "\n";
    cout << "f´(" << x << "): " << function << endl;
    cout << "error: " << error(x, h, function) << "%\n";
}

int main()
{
    float x = 0.5;
    float h = 0.5;
    cout << endl
         << "Valor real de la derivada: " << f_prime(x) << endl;
    method("Forward difference", x, h, forward_diff(x, h));
    method("Backward difference", x, h, backward_diff(x, h));
    method("Central difference", x, h, central_diff(x, h));
    return 0;
}