def calculate(distance,no_of_passengers):
    cost = (distance/10)*70
    sales  = no_of_passengers * 80
    profit = sales - cost
    if profit<0:
        return -1
    return profit



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))