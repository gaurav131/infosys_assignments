Number=int(input('Number'))
temp=Number
reverse=0
while(Number!=0):
    remainder=Number%10
    reverse=reverse*10+remainder
    Number=Number//10
if temp==reverse:
    print('Palindrome')
else:
    print('Not a Palindrome')

