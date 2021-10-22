import scipy.misc as dv
from numpy import array
import sympy as sp
from math import factorial

class Taylor:
    def __init__(self, var, iterator, function):
        self.function = None
        self.str_function = function
        self.x_symbol = sp.Symbol('x')
        self.x_var = var
        self.iter = iterator
        self.true_value = None
        x = self.x_symbol
        self.function = eval(function) 


    def symbolic_derivative(self) -> array:
        derivatives = []
        for i in range(self.iter):
            derivatives.append(sp.diff(self.function, self.x_symbol, i))

        return derivatives

    def numeric_derivative(self,h) -> array:
        numeric_values = []
        x = self.x_var
        h = h
        fisrt_term = self.str_function.replace('x', str(x))
        
        self.true_value = eval(self.str_function.replace('x', str(h)))

        numeric_values.append(eval(fisrt_term))

        for ec in self.symbolic_derivative():
            def f(x): return eval(str(ec))
            numeric_values.append(dv.derivative(f, self.x_var, dx=1e-6))
           
        return numeric_values

    def taylor(self, n, h)->dict:
        series = []
        result = 0
        res = []
        sum = []
        for i in range(n):
            series.append((self.numeric_derivative(h)[i] / factorial(i))*(h)**i)
            result += series[i]
            sum.append(round(result, 4))
            res.append(self.true_value - round(sum[i],4))


        return {
            "Sumas": sum,
            "Suma total": round(result, 4),
            "errores": res,
            "terminos":series,
        }
