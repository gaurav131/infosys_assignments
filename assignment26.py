
def solve(heads,legs):
    for i in range(heads+1):
        j=heads-i
        if (2*i)+(4*j)==legs:
            print (i,j)
            return
    print("No solution")

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count



    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(38,131)