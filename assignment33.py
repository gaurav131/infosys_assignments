def find_common_characters(msg1,msg2):
    data = [x for x in msg1 if x in msg2 and x!=" "]
    unique = []
    for x in data:
        if x not in unique:
            unique.append(x)
    if len(unique)==0:
        return -1
    return "".join(unique)
#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)