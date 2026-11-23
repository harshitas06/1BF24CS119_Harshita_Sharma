
# FOL to CNF Conversion (Basic SymPy Version)

from sympy import symbols
from sympy.logic.boolalg import (
    Implies, Equivalent, to_cnf
)

# Step 1: Define propositions
P, Q, R = symbols('P Q R')

# Step 2: Take a logical expression
expr = Implies(P, Q & R)

print("Original Expression:")
print(expr)

# Step 3: Remove implication
step1 = (~P) | (Q & R)
print("\nAfter removing implication:")
print(step1)

# Step 4: Apply De Morgan's law if needed
step2 = step1
print("\nAfter moving NOT inward:")
print(step2)

# Step 5: Distribute OR over AND
cnf = to_cnf(expr, simplify=True)

print("\nFinal CNF:")
print(cnf) 
