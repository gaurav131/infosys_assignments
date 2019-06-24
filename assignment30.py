def encode(message):
    a = [message[0]]
    b = []
    count = 0
    message+="1"
    for x in message[1:]:
        if a[-1] == x:
            count+=1
        else: 
            count+=1
            b.append((a[-1],count))
            count = 0
        a.append(x)
    encoded_message = ""
    for x,y in b:
        encoded_message += str(y)+str(x)
    return encoded_message

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)