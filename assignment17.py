def new_salary(salary,level):
    if level<3 or level>5:
        return salary
    elif level == 3:
        return salary + (salary*0.15)
    elif level == 4:
        return salary + (salary*0.7)
    return salary + (salary*0.5)
print(new_salary(25000,3))