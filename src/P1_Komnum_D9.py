import matplotlib.pyplot as plt 
from matplotlib import animation
import numpy as np


print("Metode Bolzano")

def f(x):
    return 3*x**3 - 100 + 2*x

def bisection(a, b, n):
    xLeft = a
    xRight = b
    for i in range(n):

        c = (xLeft + xRight) / 2.0
        prod = f(xLeft) * f(c)

        if prod > 0:
            # + + -
            # - - +
            xLeft = c

        elif prod < 0:
            # + - -
            # - + +
             xRight = c

    return xLeft, xRight

xMin, xMax = 0, 5
yRange = f(xMin), f(xMax)
yMin, yMax = min(yRange), max(yRange)
vf = np.vectorize(f)
x = np.linspace(xMin, xMax)
y = vf(x)
epsilon = 0.1

fig = plt.figure()
ax = plt.axes(xlim = (xMin - epsilon, xMax + epsilon), ylim = (yMin, yMax))
curve, = ax.plot([],[], color = 'blue')
left, = ax.plot([], [], color ='red')
right, = ax.plot([], [],  color ='red')

def init():
    curve.set_data([], [])
    left.set_data([], [])
    right.set_data([], [])
    return left, right, curve,

def animate(frame):
    a, b = bisection(xMin, xMax, frame)
    print(f"f(x1) : {a:.10f} \t f(x2) : {b:.10f}")
    left.set_data([a, a], [yMin, yMax])
    right.set_data([b, b], [yMin, yMax])
    curve.set_data(x, y)
    return left, right, curve

anim = animation.FuncAnimation(fig, animate, init_func = init, frames= 15, interval = 300, blit = True)



plt.title("Bolzano Method")
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.grid()
plt.show()


        
