def create_largest_number(number_list):
    a = max(number_list)
    number_list.remove(a)
    b = max(number_list)
    number_list.remove(b)
    return int(str(a)+str(b)+str(number_list[0]))

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)