# Viết chương trình cho phép người dùng nhập vào 1 số nguyên (n), kiểm tra số n có phải là số chẵn hay số lẻ không. In ra màn hình kết quả tương ứng. Ví dụ: n = 2 => in ra màn hình
# Input
n = int(input('Nhập vào số nguyên n: '))
# Output
ket_qua = ''
# process
if n % 2 == 0:
    ket_qua = f'{n} là số chẵn'
else:
    ket_qua = f'{n} là số lẻ'
print(ket_qua)