def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func:
        return sum(filter_func(list_of_num))
    return sum(list_of_num)

def even(data):
    return [x for x in data if x%2==0]

def odd(data):
    return [x for x in data if x%2!=0]

sample_data = range(1,11)
print(sum_of_numbers(sample_data,odd))