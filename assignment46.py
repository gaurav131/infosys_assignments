def nearest_palindrome(number):
    while True:
        number+=1
        if number == int(str(number)[::-1]):
            return number

number=12300
print(nearest_palindrome(number))