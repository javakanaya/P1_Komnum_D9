print("Its Running v1.0")

def f(x):
    return 10**x - 100 + 2*x

def bisection(a, b, tolearnce):
    xLeft = a
    xRight = b
    while(abs(xLeft - xRight) >= tolearnce):
        
        c = (xLeft + xRight) / 2.0
        prod = f(xLeft) * f(c)

        if prod > 0:
            xLeft = c
        
        else:
            if prod < 0:
                xRight = c


    return c

answer = bisection(-5, 5, 1e-5)
print("Bolzano method give result at x= %.5f" % answer)

        