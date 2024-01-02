# Viết chương trình cho phép người dùng nhập vào số lương cơ bản 1 giờ và tổng giờ làm. Yêu cầu: tình lương theo công thức sau:
# Nếu làm việc từ 40 tiếng trở xuống thì tong_luong=luong_cb * so_gio_lam
# Nếu làm việc hơn 40 tiếng thì lương từ tiếng thứ 40 trở đi sẽ tính theo hệ số 1.5

# Input
luong_cb = float(input("Nhập lương cơ bản: "))
so_gio_lam = float(input("Nhập số giờ làm: "))
# Output
tong_luong = 0
# Process
if so_gio_lam <= 40:
    # pass
    tong_luong = luong_cb * so_gio_lam
else:
    tong_luong = (luong_cb * so_gio_lam) + (luong_cb * (so_gio_lam - 40) * 1.5)

print(f'Tổng lương: {tong_luong}')