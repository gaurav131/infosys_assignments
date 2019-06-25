list_of_marks=(0,0,0,0,0,0,0,0,0,0)
import statistics
def find_more_than_average():
    mean = statistics.mean(list_of_marks)
    count = 0
    for i in list_of_marks:
        if i>mean:
            count+=1
    return count*10
    #Remove pass and write your logic here

def sort_marks():
    s_list = list(list_of_marks)
    s_list.sort()
    return s_list
    #Remove pass and write your logic here

def generate_frequency():
    freq = [0]*26
    for x in range(max(list_of_marks)+1):
        if x in list_of_marks:
            count = list_of_marks.count(x)
        else:
            count = 0
        freq[x]=count
    
    return freq
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())