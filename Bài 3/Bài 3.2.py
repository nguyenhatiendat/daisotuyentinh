#thực hành bài tập 5
import numpy as np
M1=np.array([[9,12],
            [23,30]])
u=np.array([2,1])
#M1.u
tichM1u=M1.dot(u)
print("M1.dot(u):",tichM1u)
#u.M1
tichuM1=u.dot(M1)
print("u.dot(M1):",tichuM1)
#np.dot
print("np.dot(M1, u):",np.dot(M1,u))
print("np.dot(u, M1):",np.dot(u,M1))


mat1=np.zeros((5,5))
print("mat1:\n",mat1)
mat2=np.ones((5,5))
print("mat2:\n",mat2)
mat3=mat1+2*mat2
print("mat3=mat1+2*mat2:\n",mat3)
mat4=mat3
mat4[1][1]=10
print("mat4 sau khi đổi phần tử [1][1]:\n",mat4)
print("mat3 có thay đổi không (tham chiếu):\n",mat3)
mat5=np.copy(mat3)
mat5[1][2]=10
print("mat5 sau khi đổi phần tử [1][2]:\n",mat5)
print("mat3 có thay đổi không:",mat3)
mat6=np.empty((14,5))
print("mat6 (giá trị rỗng):\n",mat6)
mat7=np.random.rand(14,5)
print("mat7 (ngẫu nhiên 0-1):\n",mat7)
mat8=np.random.randint(1,5,size=(14,5))
print("mat8 (nguyên trong [1, 4)):\n",mat8)

