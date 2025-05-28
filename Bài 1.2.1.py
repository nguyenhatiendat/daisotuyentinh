danhsach1=[1.,3.] 
danhsach2=[5.,7.] 
danhsach=danhsach1+danhsach2
print(danhsach)
danhsach_gapdoi=2*danhsach
print(danhsach_gapdoi)
print(danhsach*2)
#Lỗi không thể chia danh sách
try:
    print("danhsach/2=",danhsach/2)
except TypeError:
    print("Lỗi khi chia danh sách")

#ghép danh sách bằng lệnh zip
mon_hoc=["ToanCC","DSTT","ToanRR","LaptrinhCB"] 
thu_tu=[2,3,4,1] 
diem_so=[10,9,8,7] 
anh_xa=zip(thu_tu,mon_hoc,diem_so)
anh_xa_list=list(anh_xa)
print(anh_xa_list)
tap_hop=set(anh_xa_list)
print(tap_hop)
lay_TT,lay_monhoc,lay_diem=zip(*anh_xa_list)
print("lay_monhoc=",lay_monhoc)
import itertools
tap_sinh=list(itertools.chain(range(4),range(5,10),range(15,20)))
print("tap_sinh =",tap_sinh)
kq=list(zip(range(4),range(7, 12),reversed(range(11))))
print("ket_qua=",kq)