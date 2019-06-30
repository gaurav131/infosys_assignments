def find_ten_substring(num_str):
	if num_str[0]=='-':
		num_str=num_str[1:]
	sum=0
	start=0
	end=0
	l=[]
	for d in num_str:
		end+=1
		sum+=int(d)
		while(sum>10):
			sum-=int(num_str[start])
			start+=1
		if(sum==10):
			l.append(num_str[start:end])
	return l
num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)