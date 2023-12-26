# Viết chương trình cho phép người dùng nhập vào điểm toán, điểm văn. Yêu cầu tính và xuất ra màn hình các thông tin sau:
# điểm trung bình = (điểm toán + điểm văn)/2
# Xếp loại:
#   điểm trung bình < 5: loại yếu
#   5 <= điểm trung bình < 6.5: loại trung bình
#   6.5 <= điểm trung bình < 8: loại khá
#   8 <= điểm trung bình < 10: loại giỏi
#   còn lại không thể xếp loại

# Input: 
diem_toan = float(input("Nhập điểm toán: "))
diem_van = float(input("Nhập điểm văn: "))
# Output:
diem_trung_binh = 0.0
xep_loai = ""
# Process
diem_trung_binh = (diem_toan + diem_van)/2

if diem_trung_binh < 5:
    xep_loai = "Yếu"
elif 5 <= diem_trung_binh < 6.5:
    xep_loai = "Trung bình"
elif 6.5 <= diem_trung_binh < 8:
    xep_loai = "Khá"
elif 8 <= diem_trung_binh <= 10:
    xep_loai = "Giỏi"
else:
    xep_loai = "Không thể xếp loại"

print(f'Điểm trung bình là: {diem_trung_binh}')
print(f'Xếp loại: {xep_loai}')
