from sympy import symbols, Symbol, factor, expand, simplify, sin, cos
x,y=symbols('x y')
#biểu thức ban đầu
bieuthuc1=x**3-y**3
#phân tích thành nhân tử
print("Factor (x³ - y³):",factor(bieuthuc1))
#khai triển biểu thức
bieuthuc2=(x-y)*(x**2+x*y+y**2)
print("Expand ((x-y)(x²+xy+y²)):",expand(bieuthuc2))
#thay thế giá trị
bieuthuc3=x**2-x*y+y**2
#TH1: thay x=3,y=x
giatri1=bieuthuc3.subs({x:3,y:x})
print("TH1 - Thay x=3,y=x:",giatri1)
# TH2: thay x=y và y=3
giatri2=bieuthuc3.subs({x:y,y:3})
print("TH2 - Thay x=y, y=3:",giatri2)
#TH3: thay y=x rồi x=3
giatri3=bieuthuc3.subs({y:x}).subs({x:3})
print("TH3 - Thay y=x rồi x=3:",giatri3)
#simplify biểu thức
#thay x=1-y vào biểu thức
x_new,y_new=Symbol('x'),Symbol('y')
bieuthuc4=x_new**2-x_new*y_new+y_new**2
bieuthuc4_moi=bieuthuc4.subs({x_new:1-y_new})
print("Biểu thức sau khi thay x=1-y:",bieuthuc4_moi)
#rút gọn biểu thức bằng simplify
dongian=simplify(bieuthuc4_moi)
print("Simplify:",dongian)
#biểu thức lượng giác
bt_moi=simplify(sin(x)**2 +cos(x)**2)
print("Simplify sin²x + cos²x =",bt_moi)
