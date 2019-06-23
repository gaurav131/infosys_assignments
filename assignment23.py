def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    cost  = dict(zip(gems_list,price_list))
    for x in reqd_gems:
        if x not in cost.keys():
            bill_amount = -1
            return bill_amount
    if 0 in reqd_quantity:
        return -1
    amount = []
    requirement = dict(zip(reqd_gems,reqd_quantity))
    for x in requirement.keys():
        amount.append(cost[x] * requirement[x])
    bill_amount = sum(amount)
    if bill_amount > 30000:
        bill_amount = bill_amount - bill_amount*0.05
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)