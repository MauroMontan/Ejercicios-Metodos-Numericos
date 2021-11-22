// bisection method
#include <iostream>
#include <cmath>

using namespace std;

float f(float x)
{
    return pow(x, 4) + 3 * pow(x, 3) - 2;   
}

float bisection(float a, float b, float tol)
{
    float c = (a + b) / 2;
    if (fabs(f(c)) < tol)
    {
        return c;
    }
    if (f(a) * f(c) < 0)
    {
        return bisection(a, c, tol);
    }
    else
    {
        return bisection(c, b, tol);
    }
}

int main()
{    
    float a = 0;
    float b = 1;
    float tol = 0.00001;
    cout << bisection(a, b, tol) << endl;
    return 0;
}