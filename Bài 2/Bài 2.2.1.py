from sympy import symbols, factor, expand
x,y=symbols('x y')
b1=x**3-y**3
print("Biểu thức ban đầu:",b1)
print("Biểu thức sau khi factor():",factor(b1))
b2=(x-y)*(x**2+x*y+y**2)
print("\nBiểu thức ban đầu:",b2)
print("Biểu thức sau khi expand():",expand(b2))
