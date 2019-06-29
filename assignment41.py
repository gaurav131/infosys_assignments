def find_ten_substring(Number):
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
num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)