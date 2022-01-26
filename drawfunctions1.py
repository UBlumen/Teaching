import numpy as np
import math as m
import matplotlib.pyplot as plt


#xval = np.linspace(-5, 5, 32)
xval = np.linspace(-4, 4, 60)
#xval = np.linspace(-3, 3, 13)

yval1 = np.exp(xval)
yval2 = np.exp(-xval)
yval3 = np.cosh(xval)
yval4 = np.sinh(xval)
yval5 = np.tanh(xval)
yval6 = np.log(xval)
yval7 = np.log(1+xval)
sig = 1
mu = 0
yval8 = np.exp(-0.5*(xval-mu)**2/sig**2)/(sig*np.sqrt(2*np.pi))
yval9 = np.exp(-xval**2+2*xval)
yval10 = np.exp(-xval**2)

plt.plot(xval, yval1, color = 'rosybrown', marker = "o", label="exp(x)")
plt.plot(xval, yval2, color = 'firebrick', marker = "o", label="exp(-x)")
plt.plot(xval, yval3, color = 'forestgreen', marker = "o", label="sinh(x)")
plt.plot(xval, yval4, color = 'royalblue', marker = "o", label="cosh(x)")
#plt.plot(xval, yval5, color = 'lightseagreen', marker = "o", label="tanh(x)")
plt.title("exponentials and hyperbolics")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

plt.plot(xval, yval7, color = 'firebrick', marker = "o", label="ln(1+x)")
plt.plot(xval, yval6, color = 'rosybrown', marker = "o", label="ln(x)")
plt.title("logs")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

plt.plot(xval, yval8, color = 'firebrick', marker = "o", label="Gaussian")
plt.plot(xval, yval10, color = 'forestgreen', marker = "o", label="exp(-x**2)")
plt.plot(xval, yval9, color = 'royalblue', marker = "o", label="exp(-x**2+2x)")
plt.title("Gaussian etc")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
