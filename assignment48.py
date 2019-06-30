def find_correct(word_dict):
    correct,almost,incorrect=0,0,0
    for key,value in word_dict.items():
        count=0
        if(key==value):
            correct+=1
        elif(len(key)==len(value)):
            for i in range(0,len(key)):
                if(key[i]!=value[i]):
                    count+=1
            if(count<=2):
                almost+=1
            else:
                incorrect+=1
        else:
            incorrect+=1
    return [correct,almost,incorrect]

word_dict = {"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))