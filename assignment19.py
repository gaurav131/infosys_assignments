def order(food,quantity,distance):
    food_cost = {"V":120,"N":150}
    if food.upper() == "V" or food.upper() == "N":
        if distance <= 0 or quantity < 1:
            return ("the bill amount to be paid is ", -1)
        if distance<=3:
            delivery = 0
        elif distance <= 6:
            delivery = (distance-3)*3
        else:
            delivery = 9+((distance-6)*6)
        return ("Total amount to be paid is", 
            (food_cost[food.upper()]*quantity)+delivery)
    else:
        return ("the bill amount to be paid is ", -1)
print(order("V",5,9))
    
