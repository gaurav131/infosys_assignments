def find_correct(word_dict):
    correct = 0
    almost = 0
    wrong = 0
    for i in word_dict.keys():
        match = 0
        count = len(i)-1
        while count>=0:
            if i[count]!=word_dict[i][count]:
                match+=1
            count-=1
        if match == 0:
            correct+=1
        elif match <=2:
            almost += 1
        else:
            wrong += 1
    return [correct,almost,wrong]

word_dict = {"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))