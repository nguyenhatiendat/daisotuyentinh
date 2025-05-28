import numpy as np
vec1=np.array([1,3,5])
print("vec1*2:",vec1*2)
print("vec1+vec1:",vec1+vec1)
print("vec1/2:",vec1/2)
vec2=np.array([2,4])
print("vec1[:2]+vec2:",vec1[:2]+vec2)
vec3=np.array([2,4,6])
print("vec1+vec3:",vec1+vec3)
print("vec1/vec3:",vec1/vec3)
print("2*vec1+5*vec3:", 2*vec1+5*vec3)

v=np.array([1,3,5])
#tổng các phần tử
print("Tổng:",np.sum(v))
#số chiều
print("Shape:",v.shape)
#chuyển vị
print("Transpose:",v.T)
#truy xuất phần tử
print("v[1]:",v[1])
print("v[0]:",v[0])
print("v[-1]:",v[-1])
print("v[2]:",v[2])
print("v[1:2]:",v[1:2])
v2=[4,6]
v3=2*v[2]+v[1]*3
print("v3:",v3)
print("v3-v2:",np.array([v3,v3])-v2)
#toán tử lượng giác
print("sqrt(10):",np.sqrt(10))
print("cos(3):",np.cos(3))
print("sin(3):",np.sin(3))
#tích vô hướng
v1=np.array([1,3])
v3=np.array([2,4])
print("np.dot(v1,v3):", np.dot(v1,v3))
print("v1.dot(v3):",v1.dot(v3))
print("v3.dot(v1):",v3.dot(v1))

