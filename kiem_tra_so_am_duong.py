# Viết chương trình nhập vào số nguyên n và kiểm tra xem nó làm số âm hay số dương. Xuất kết quả ra màn hình
# Input
so_nguyen = int(input("Nhập số nguyên n: "))
# Output
ket_qua = ""
# Process
if so_nguyen < 0:
    ket_qua = f'{so_nguyen} là số âm'
else:
    ket_qua = f'{so_nguyen} là số dương'

print(ket_qua)