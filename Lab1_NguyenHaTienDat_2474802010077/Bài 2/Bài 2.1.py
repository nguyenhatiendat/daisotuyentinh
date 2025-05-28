from sympy import Symbol, symbols, expand
# Định nghĩa biến symbol
x=Symbol('x')
y=Symbol('y')
z=Symbol('z')
# Các biểu thức đơn giản
f=x+x+2
print("f =", f)
# Biểu thức với các tên biến khác
a=Symbol('Noi')
b=Symbol('Chim')
expr1=3*b+7*a
print("expr1=",expr1)
# Hiện tên của symbol
print("Tên của a:",a.name)
print("Tên của b:",b.name)
# Định nghĩa nhiều biến cùng lúc
a,b,c=symbols('a b c')
print("a, b, c =",a,b,c)
# Các phép toán với biểu thức
x=Symbol('x')  # Đặt lại để đảm bảo chính xác
y=Symbol('y')
s=x*y+y*x
print("s=",s)
# Phép nhân
p=x*(x+2*x)
print("p =",p)
# Biểu thức chưa triển khai (chưa rút gọn)
p=(x+2)*(y+3)
print("Biểu thức chưa triển khai: p=",p)
# Triển khai biểu thức (expand)
print("Biểu thức sau khi expand:",expand(p))
# Biểu thức phức hợp khác
p=(x+2)*(y+3)+(x+2)*(x-3)
print("Biểu thức phức hợp p=",p)
# Triển khai biểu thức
print("Biểu thức phức hợp sau khi expand:",expand(p))
# Biểu thức đơn giản sẽ được SymPy rút gọn tự động
p=x*(-x+2*x-x)
print("Biểu thức đơn giản tự động rút gọn: p =",p)
