import randomizer
from matplotlib.pyplot import  plot, xlabel, ylabel, title, legend, show
from numpy import linspace

x_end, y_end = randomizer.randomPair(-10, 10)
x = linspace(0, x_end, 100)

plot(x, x*y_end/x_end, label="desired graph")
print (x_end, y_end)

title ("Homework")
legend()
show()
