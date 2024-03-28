# Dựa vào các kiến thức đã được giảng viên hướng dẫn, các bạn sẽ tạo ra một chương trình cho phép người dùng nhập vào 3 số nguyên và sẽ sắp xếp lại các số nguyên đó theo thứ tự tăng dần và in ra màn hình.

# Input
number_1 = int(input('Nhập vào một số nguyên 1: '))
number_2 = int(input('Nhập vào một số nguyên 2: '))
number_3 = int(input('Nhập vào một số nguyên 3: '))

# Process
if number_1 < number_2 < number_3:
    print(f'Thứ tự số nguyên là: {number_1}, {number_2}, {number_3}')
elif number_2 < number_1 < number_3:
    print(f'Thứ tự số nguyên là: {number_2}, {number_1}, {number_3}')
elif number_2 < number_3 < number_1:
    print(f'Thứ tự số nguyên là: {number_2}, {number_3}, {number_1}')
elif number_3 < number_1 < number_2:
    print(f'Thứ tự số nguyên là: {number_3}, {number_1}, {number_2}')
elif number_3 < number_2 < number_1:
    print(f'Thứ tự số nguyên là: {number_3}, {number_2}, {number_1}')
else:
    print(f'Thứ tự số nguyên là: {number_1}, {number_3}, {number_2}')
