#lưu ý các phép toán xử lý trên list
danhsach1=[1.,3.] 
danhsach2=[5.,7.] 
danhsach=danhsach1+danhsach2
print("Tổng danh sách: ",danhsach)
danhsach_gapdoi=2*danhsach
print("Tổng danh sách gấp đôi: ",danhsach_gapdoi)
print("Tổng danh sách nhân hai: ",danhsach*2)
#Lỗi không thể chia danh sách
try:
    print("danhsach/2=",danhsach/2)
except TypeError:
    print("Lỗi khi chia danh sách")
    ketqua=[x/2 for x in danhsach]
    print("Kết quả chia từng phần tử trong danh sách: ",ketqua)

#ghép danh sách bằng lệnh zip
mon_hoc=["ToanCC","DSTT","ToanRR","LaptrinhCB"] 
thu_tu=[2,3,4,1] 
diem_so=[10,9,8,7] 
anh_xa=list(zip(thu_tu,mon_hoc,diem_so))
print("Zip: ",anh_xa)
tap_hop=set(anh_xa)
print("Set: ",tap_hop)
lay_TT,lay_monhoc,lay_diem=zip(*anh_xa)
print("Thứ tự: ",lay_TT)
print("Môn học: ",lay_monhoc)
print("Điểm số: ",diem_so)
import itertools
tap_sinh=list(itertools.chain(range(4),range(5,10),range(15,20)))
print("tap_sinh =",tap_sinh)
kq=list(zip(range(4),range(7, 12),reversed(range(11))))
print("ket_qua=",kq)