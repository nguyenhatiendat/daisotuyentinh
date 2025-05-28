import numpy as np
A=np.array([[1, 1, 0, 0, 1],
              [3, 1, 0, 1, 1],
              [5, 2, 0, 1, 2],
              [2, 0, 1, 2, 3]])
B=np.array([[1, 1, 2, 2, 1],
              [2, 2, 2, 0, 2],
              [0, 1, 2, 4, 2],
              [1, 4, 1, 2, 2]])
C=np.array([[0, 5, 1, 1, 1],
              [0, 1, 1, 1, 3],
              [1, 3, 1, 3, 1],
              [0, 1, 3, 3, 0]])
D=np.array([[3, 1, 1, 0, 1],
              [5, 0, 0, 3, 7],
              [7, 0, 0, 3, 5],
              [5, 0, 3, 5, 3]])
E=np.array([[0, 0, 0,10, 0],
              [0, 0,15, 0, 0],
              [0, 5,15, 5, 0],
              [0,20, 5, 0, 0]])
def get_safe_mask(*layers):
    total=sum(layers)
    return (total<=5).astype(int),total
scenarios={
    'a. Chiến dịch ngắn hạn (chỉ xét lộ bí mật)':[E],
    'b. Tập luyện thời bình (không xét lộ bí mật và bệnh dịch)':[A,B,C],
    'c. Mùa khô (không lũ, không sạt nhưng có cháy và bệnh)':[A,C,D],
    'd. Mùa mưa (có lũ, sạt, bệnh nhưng không cháy)':[B,C,D],
    'e. 8 tháng (xét toàn bộ nguy cơ)':[A,B,C,D,E],
    }
for name,layers in scenarios.items():
    mask,total=get_safe_mask(*layers)
    print(f"\n{name}")
    print("Tổng nguy cơ:")
    print(total)
    print("Mặt nạ an toàn (1=an toàn, 0=nguy hiểm):")
    print(mask)
