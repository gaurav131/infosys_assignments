def pal(s,i=-1):
    s = s.lower()
    if len(s)<=1:
        return True
    i+=1
    return s[i]==s[-1] and pal(s[i:-1],i)
pal("Meem")