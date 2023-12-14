# Viết chương trình cho phép người dùng nhập vào họ tên và tiền lương, số giờ làm việc
# In ra màn hình các thông tin sau: Họ tên, tổng lương (tiền lương * số giờ làm việc)

# Input
ho_ten = input('Nhập họ và tên: ')
tien_luong = input('Nhập tiền lương: ')
so_gio_lam = input('Nhập số giờ làm: ')

# Process
tong_luong = float(tien_luong) * float(so_gio_lam)

# Output
print(f'Họ tên: {ho_ten}, tổng lương: {str(tong_luong)}')