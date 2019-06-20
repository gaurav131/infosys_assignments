def order(food,quantity,distance):
    food_cost = {"V":120,"N":150}
    if food.upper() not in food_cost.keys() or distance <= 0 or quantity < 1 :
            return ("the bill amount to be paid is ", -1)     
    else:
        if distance<=3:
            delivery = 0
        delivery = (distance-3)*3 if distance <= 6 and distance>3 else 9+((distance-6)*6)  
        return ("Total amount to be paid is", 
            (food_cost[food.upper()]*quantity)+delivery)
print(order("V",5,9))

