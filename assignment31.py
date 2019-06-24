def check_palindrome(word):
    x = word.lower()
    return x == x[::-1]

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")