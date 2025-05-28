def tao_danhsach():
    return [100,200,300]
#Reset giá trị trước
a=b=c=0
print("Trước khi gán lại:",a,b,c)
#Gọi hàm và gán lại
mylist=tao_danhsach()
a,b,c=mylist
print("Sau khi gán lại:",a,b,c)
