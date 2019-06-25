def find_pairs_of_numbers(num_list,n):
    count = 0
    l = []
    for x in num_list:
        for i in num_list:
            if x+i == n and x!=i:
                if (x,i) in l or (i,x) in l:
                    continue
                l.append((x,i))
                count+=1
    return count

num_list=[10,20,30,40,50]
n=90
print(find_pairs_of_numbers(num_list,n))