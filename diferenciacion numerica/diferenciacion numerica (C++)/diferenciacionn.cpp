#include <iostream>
#include <cmath>
using namespace std;

double f(double x);
double f_prima(double x);
double centrada(double x, double h);
double hacia_adelante(double x, double h);
double hacia_atras(double x, double h);
double error(double x, double h, double diferencia);

int main()
{
    float x, h;
    cout << "ingresa el valor de x: ";
    cin >> x;
    cout << "ingresa el valor de h: ";
    cin >> h;
    cout << "\n";

    float hd = hacia_adelante(x, h);
    float ha = hacia_atras(x, h);
    float c = centrada(x, h);

    cout << "f(x) = " << f(x) << "\n";
    cout << "f'(x) = " << f_prima(x) << "\n";
    cout << "\n";

    cout << "hacia delante" << endl;
    cout << "f(x+h) = " << hd << endl;
    cout << "error = " << error(x, h, hd) << "%" << endl;
    cout << "\n";

    cout << "hacia atras" << endl;
    cout << "f(x-h) = " << ha << endl;
    cout << "error = " << error(x, h, ha) << "%" << endl;
    cout << "\n";

    cout << "centrada" << endl;
    cout << "f(x) = " << c << endl;
    cout << "error = " << error(x, h, c) << "%" << endl;
    cout << "\n";

    return 0;
}

// Funcion a la cual se le aplicara la diferenciacion
double f(double x)
{
    //f(x) = -0.1*x**4 - 0.15*x**3 - 0.5*x**2 -0.25*x + 1.2

    return -0.1 * (pow(x, 4)) - 0.15 * (pow(x, 3)) - 0.5 * (pow(x, 2)) - 0.25 * x + 1.2;
}

// Derivada de la funcion, servira para calcular el error
double f_prima(double x)
{
    return -0.4 * (pow(x, 3)) - 0.45 * (pow(x, 2)) - 1 * x - 0.25;
}

// Funcion que calcula la diferenciacion central
double centrada(double x, double h)
{
    return (f(x + h) - f(x - h)) / (2 * h);
}

// Funcion que calcula la diferenciacion hacia adelante
double hacia_adelante(double x, double h)
{
    return (f(x + h) - f(x)) / h;
}

//Funcion que calcula la diferenciacion hacia atras
double hacia_atras(double x, double h)
{
    return (f(x) - f(x - h)) / h;
}

// Funcion que calcula el error de la diferenciacion
double error(double x, double h, double diferencia)
{
    return abs((f_prima(x) - diferencia) / f_prima(x) * 100);
}