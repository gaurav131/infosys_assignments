n = 5 #user input
b = (n*2)-1 
a = [n]*b
mn = [a]
for i in range(1,(b//2)+1):
	c = a[i:-i]
	for x in range(len(c)):
		c[x] = n - i
	mn.append(mn[-1][:i]+c+mn[-1][-i:])
mn2 = mn[:-1]
mn2.reverse()
mn.append(mn2)