def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    amount_1 = no_of_one
    amount_5 = no_of_five * 5
    if (amount_5+amount_1)< rupees_to_make:
        print(-1)
        return
    five_needed = rupees_to_make//5
    one_needed = rupees_to_make%5
    if amount_5<rupees_to_make:
        one_needed = rupees_to_make-amount_5
        print("No. of Five needed :", no_of_five)
        print("No. of One needed  :", one_needed)
        return
    if amount_1<one_needed:
        print(-1)
        return -1

    print("No. of Five needed :", five_needed)
    print("No. of One needed  :", one_needed)
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)    

    
