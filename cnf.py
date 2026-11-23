
from sympy import symbols
from sympy.logic.boolalg import Implies, Equivalent, to_cnf

# Define variables
P, Q, R = symbols('P Q R')

# Create logical expression
expression = Implies(P, Q & R)

# Display original expression
print("Original Expression:")
print(expression)

# Convert into CNF
cnf = to_cnf(expression)

# Display CNF
print("\nCNF Expression:")
print(cnf)
