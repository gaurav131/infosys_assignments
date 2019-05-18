l=[]
s=input("String : ")#"([(]))"
pair_for_closed={')':'(','}':'{',']':'['}
open_counts={'(':0,'[':0,'{':0}
for c in s:
	print(open_counts,l)
	if(c in open_counts):
		l.append(c)
		open_counts[c]+=1
	elif(c in pair_for_closed):
		if(l.pop()==pair_for_closed[c]):
			open_counts[pair_for_closed[c]]-=1
		else:
			print('Invalid')
			exit(1) 
print(open_counts) 
if any(open_counts.values()):
	print('Invalid')
else:
	print('Valid')