m = input()
str_list = []
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum_number = 0
for i in m:
    if i in num_list:
        sum_number += int(i)
    else:
        str_list.append(i)
print(''.join(sorted(str_list)), sum_number, sep='')
