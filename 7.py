sum=0
choice=input('Choice:(Yes/No): ').lower()
while(choice=='yes' or choice=='y'):
    Number=int(input('Number: '))
    if(Number%4==0):
        sum+=Number
    choice=input('Choice:(Yes/No): ').lower()
print(sum)   