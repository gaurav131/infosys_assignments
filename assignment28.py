def find_max(num1, num2):
    max_num=-1
    if num2> num1:
        data = range(num1,num2+1)
        main_list = []
        for x in data:
            b = str(x)
            if "-" in str(x):
                b = str(x)[1:]
            sx = list(map(int,list(b)))
            if len(sx)==2 and sum(sx)%3==0 and x%5==0:
                main_list.append(x)
        if len(main_list)!=0:
            return max(main_list)
        
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,100)
print(max_num)