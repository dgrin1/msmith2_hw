from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show

gamma= 1.2e-4 #yr^-1
def f(x,t):
    return -gamma*x

a = 0.0
b = 560000.0
N = 25
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
x = 100.0

for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

plot(tpoints,xpoints)
xlabel("t")
ylabel("x(t)")
show()
