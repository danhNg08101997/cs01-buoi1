#=============== Toán tử số học trong Python ===================
a:int = 5
b:int = 10

#Phép cộng
tong = a + b
print("Tổng ", tong)

#Phép trừ
hieu = a-b
print("Hiện ", hieu)

#Tích
tich = a*b
print("Tích ", tich)

# Thương
thuong = b/a
print("Thương ", thuong)

# chia lấy phần nguyên
phan_nguyen = 5 // 2 
print("Phần nguyên ", phan_nguyen)

# chia lấy phần dư
phan_du = 5 % 2
print("Phần dư ", phan_du)

# phép lũy thừa
luy_thua = 5**3 #5 * 5 * 5
print("Lũy thừa ", luy_thua)

# ======================= Phép tính trên chuỗi ===========================
tieu_de = 'Chào mừng bạn'
ho_ten = 'Thanh Danh'
# Phép nối chuỗi (+ chuỗi)
ket_qua = tieu_de + " " + ho_ten
print("Kết quả ", ket_qua)
# Format string: đưa 1 giá trị vào chuỗi
print(f'Chào mừng {ho_ten} đã đến với techx.edu.com')
# Phép tính trên chuỗi và số
luong = "1000"
thuong = "200"

print("Tổng lương = ", float(luong)+float(thuong)) #Phép ép kiểu