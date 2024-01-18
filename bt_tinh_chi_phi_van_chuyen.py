# Ở bài tập này, các bạn sẽ viết một chương trình tính chi phí vận chuyển hàng hoá cho đơn vị vận chuyển Viettel dựa trên khoảng cách và khối lượng hàng hoá. Các đơn vị đo khoảng cách và khối lượng hàng hoá được định nghĩa dựa trên dữ liệu người dùng nhập vào
# Công thức tính khối lượng và khoảng cách
    # Với khối lượng dưới 3kg thì tính 20000đ/kg
    # Với khối lượng trên 3kg thì tính 30000đ/kg
    # Với khoảng cách dưới 10km thì tính 20000đ/km
    # Với khoảng cách trên 10km thì tính 30000đ/km

# Input
khoi_luong = float(input('Nhập khối lượng(kg): '))
khoang_cach = float(input('Nhập khoảng cách(km): '))
# Output
chi_phi_van_chuyen = 0
# Process
chi_phi_khoang_cach = 0
chi_phi_khoi_luong = 0
khoang_phi_min = 20000
khoang_phi_max = 30000

if khoi_luong < 3 and khoang_cach < 10:
    chi_phi_khoang_cach = khoang_cach * khoang_phi_min
    chi_phi_khoi_luong = khoi_luong * khoang_phi_min
elif khoi_luong < 3 and khoang_cach >= 10:
    chi_phi_khoang_cach = khoang_cach * khoang_phi_max
    chi_phi_khoi_luong = khoi_luong * khoang_phi_min
elif khoi_luong >= 3 and khoang_cach < 10:
    chi_phi_khoang_cach = khoang_cach * khoang_phi_min
    chi_phi_khoi_luong = khoi_luong * khoang_phi_max
else:
    chi_phi_khoang_cach = khoang_cach * khoang_phi_max
    chi_phi_khoi_luong = khoi_luong * khoang_phi_max

chi_phi_van_chuyen = chi_phi_khoi_luong + chi_phi_khoang_cach

print(f'Chi phí vẫn chuyển là: {chi_phi_van_chuyen} (đồng)')