def currency_con(currency,amount):
    available_curr={"Euro":0.01417,"British Pound":0.0100,
                    "Australian Dollar":0.02140,"Canadian Dollar":0.02027}
    if currency not in available_curr.keys():
        return -1
    else:
        return ("The money you need to pay in {} is:-".format(currency), 
        	round(amount*available_curr[currency],2))
print(currency_con("Australian Dollar",200))
