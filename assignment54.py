def check_anagram(data1,data2):
    data1,data2 = data1.lower(),data2.lower()
    if len(data1)==len(data2):
        if sorted(data1.lower()) == sorted(data2.lower()):
            anagram = True
            for i,j in zip(data1,data2):
                if i == j:
                    anagram = False
            return anagram
    return False

print(check_anagram("Badcredit","Debitcard"))