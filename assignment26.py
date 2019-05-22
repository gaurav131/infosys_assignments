h = int(input('Enter No.of heads :'))
l = int(input('Enter No.of legs :'))
# fomula1
c = (4*h-l)//2
# fomula2
r = (h-c)
if(c*2+r*4 == l):
    print('No.of chickens: ',c,"\nNo.of rabbits: ",r)
else:
    print('No solution')


'''
r - rabbit
c - chicken
h - heads
l - legs

head count: h=r+c
leg count: l = r*4 + c*2

head rule
h=r+c -> r=h-c
(h-c)*4 + c*2 = l
4h-2C=l
c = (4h-l)/2
r = h-c

'''
