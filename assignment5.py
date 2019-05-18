y=int(input('Enter the year number:'))
if y%400==0 or (y%4==0 and y%100!=0):
    print('Leap year')
else:
    print('not Leap year')
