Number=input('Number: ').strip()
def find_ten_substring(Number):
	Number=str(Number)
	if '.' in Number:
		idx=Number.index('.')
		Number=Number[:idx]+Number[idx+1:]
	try:
		int(Number)
	except ValueError:
		print("Please enter a valid number")
		return None
	if Number[0]=='-':
		Number=Number[1:]
	sum=0
	start=0
	end=0
	l=[]
	for d in Number:
		end+=1
		sum+=int(d)
		while(sum>10):
			sum-=int(Number[start])
			start+=1
		if(sum==10):
			l.append(Number[start:end])
	return l
print(find_ten_substring(Number))