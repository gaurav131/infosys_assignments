def check_double(number):
    if len(str(number))==(len(str(number*2))) and number!=number*2 :
        return sorted(str(number)) == sorted(str(number*2))
    return False

print(check_double(125874))