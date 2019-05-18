Number=int(input('Number: '))
temp=Number
sum=0
while(Number!=0):
    remainder=Number%10
    sum+=remainder*remainder*remainder
    Number=Number//10

if temp==sum:
    print('Armstrong Number')
else:
    print('not Armstrong Number')
