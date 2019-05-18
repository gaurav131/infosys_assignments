def mul(x):
    m = 1
    for i in x:
        m*=i
    return m

def positive_int(*x):
    if len(x)==3:
        if 7 in x:
            idx = x.index(7)
            if idx == len(x)-1:
                return -1
            remain = x[idx+1:]
            return(mul(remain))
        else:
            return(mul(x))
    else:
        raise ValueError("Only three Positve Integers are Allowed")
print(positive_int(2,5,6))