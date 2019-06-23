def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    if num3 >= num1+num2:
        return failure
    elif num2 >= num1+num3:
        return failure
    elif num1 >= num2+num3:
        return failure
    else:
        return success

num1=3
num2=3
num3=5

form_triangle(num1, num2, num3)