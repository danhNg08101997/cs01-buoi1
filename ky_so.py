# Viết chương trình cho phép người dùng nhập vào 1 số có 3 ký số. Ví dụ: 123
# Yêu cầu tính tổng 3 ký số: 1 + 2 + 3 = 6

# Input
so = int(input("Nhập vào số nguyên có 3 chữ số: "))
# Output
tong_ky_so = 0
# process
hang_tram = so // 100
hang_chuc = so % 100 // 10
hang_don_vi = so % 100 % 10

tong_ky_so = hang_tram + hang_chuc + hang_don_vi

print(f'Tổng 3 ký số của {so} là: {hang_tram} + {hang_chuc} + {hang_don_vi} = {tong_ky_so}')
