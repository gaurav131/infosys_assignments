def pal(s):
    s = s.lower()
    if len(s)<=1:
        return True
    return s[0]==s[-1] and pal(s[1:-1])
print(pal("malaYALAM"))