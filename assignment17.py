def new_salary(current_salary,job_level):
    if job_level<3 or job_level>5:
        return current_salary
    elif job_level == 3:
        return current_salary + (current_salary*0.15)
    elif job_level == 4:
        return current_salary + (current_salary*0.07)
    return current_salary + (current_salary*0.05)
print(new_salary(25000,3))