# Viết chương trình cho phép người dùng nhập vào chiều cao (m), cân nặng. Tính và in ra màn hình BMI tương ứng
#Input
chieu_cao = float(input('Nhập chiều cao: '))
can_nang = float(input('Nhập cân nặng:'))
#Process
# chi_so_bmi = can_nang/(chieu_cao * chieu_cao)
chi_so_bmi = can_nang / chieu_cao ** 2
#Output
print(f'Chỉ số BMI là: {chi_so_bmi}')
