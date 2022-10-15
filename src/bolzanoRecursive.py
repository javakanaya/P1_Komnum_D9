print("Its Running v2.0")

def f(x):
    return 10**x - 100 + 2*x

def bisection(a, b, tolerance):
    c = (a + b) / 2.0
    if (abs(a - b) < tolerance):
        return c

    prod = f(c)*f(a)
    if(prod > 0):
        return bisection(c, b, tolerance)
    else:
        if(prod < 0):
            return bisection(a, c, tolerance)


answer = bisection(-5, 5, 1e-5)
print("Bolzano method give result at x= %.5f" % answer)


        