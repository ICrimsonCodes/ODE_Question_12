import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define variables
x = sp.Symbol('x')
y = sp.Function('y')(x)
y_p = y.diff(x)

# Define differential equation
de = sp.Eq(y*y_p, 4*x)

# Solve differential equation
C = sp.symbols('C')
y_eq = sp.dsolve(de, y, ics={y.subs(x, 1): 4})
y_eq = sp.simplify(y_eq.rhs)

# print_solution
sp.pprint(y_eq)
# Convert SymPy expression to a NumPy function
y_np = sp.lambdify(x, y_eq, 'numpy')

# Create plot
x_vals = np.linspace(0, 1)
y_vals = y_np(x_vals)
plt.plot(x_vals, y_vals)
plt.title('Solution to yy\' = 4x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
