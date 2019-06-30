def max_frequency_word_counter(data):
    data = data.split()
    word_map = {}
    for x in data:
        if x not in word_map.values():
            c = data.count(x)
            if c not in word_map.keys():
                word_map[c] = x
            else:
                if len(x) > len(word_map[c]):
                    word_map[c]=x
    word = word_map[max(word_map.keys())]
    frequency = max(word_map.keys())
    print(word,frequency)


#Provide different values for data and test your program.
data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)