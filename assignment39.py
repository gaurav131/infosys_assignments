#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,250,3]
d_menu = dict(zip(menu,quantity_available))
'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    required_item = []
    required_quantity = []
    for i in item_tuple:
        if isinstance(i,str):
            required_item.append(i)
        else:
            required_quantity.append(i)
    req = dict(zip(required_item,required_quantity))
    for i in req.keys():
        if i not in menu:
            print("{} is not available".format(i))
        elif req[i]>d_menu[i]:
            print("{} stock is over".format(i))
        else:
            print("{} is available".format(i))
    #print("<item name>is not available")
    #print("<item name>stock is over")
    #print ("<item name>is available")
    
  


'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    if index not in menu:
        return False
    if quantity_available[menu.index(index)] < quantity_requested:
        return False 
    quantity_available[menu.index(index)] -= quantity_requested
    return True


#Provide different values for items ordered and test your program
place_order("Fried Rice",2,"Soup",1)
place_order("Soup",1,"Veg Roll", 2, "Fried Rice1",1)