#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    if len(str(account_number))!=4 or str(account_number)[0]!="1":
        print("Invalid account number")
        return
    if account_balance<100000:
        print("Insufficient account balance")
        return
    criteria = {"Car":{"salary":25000,"e_loan_amount":500000,"no_of_emi":36},
                "House":{"salary":50000,"e_loan_amount":6000000,"no_of_emi":60},
                "Business":{"salary":75000,"e_loan_amount":7500000,"no_of_emi":84}}
    if loan_type not in criteria.keys():
        print("Invalid loan type or salary")
        return
    if salary <= criteria[loan_type]["salary"]:
        print("Invalid loan type or salary")
        return
    if loan_amount_expected > criteria[loan_type]["e_loan_amount"] or customer_emi_expected > criteria[loan_type]["no_of_emi"]:
        print("The customer is not eligible for the loan")
        return
    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expected
    eligible_loan_amount = criteria[loan_type]["e_loan_amount"]
    bank_emi_expected = criteria[loan_type]["no_of_emi"]

    #Use the below given print statements to display the output, in case of success
    print("Account number:", account_number)
    print("The customer can avail the amount of Rs.", eligible_loan_amount)
    print("Eligible EMIs :", bank_emi_expected)
    print("Requested loan amount:", loan_amount_expected)
    print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(2001,40000,250000,"Car",300000,30)