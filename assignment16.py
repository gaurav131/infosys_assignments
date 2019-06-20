def payment(coins,notes,amount):
    amount_1 = coins
    amount_5 = notes * 5
    if (amount_5+amount_1)< amount:
        return -1
    pd5 = amount//5
    remain = amount%5
    if amount_5<amount:
        remain_m = amount-amount_5
        return ("5rs note:-",notes,"1rs coin:-",remain_m)
    if amount_1<remain:
        return -1
    return ("5rs note:-",pd5,"1rs coin:-",remain)
print(payment(5,20,105))
    
        
    
