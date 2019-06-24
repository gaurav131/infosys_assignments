def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    count = {}
    for i in patient_medical_speciality_list:
        if isinstance(i,str):
            if i not in count.values():
                count[patient_medical_speciality_list.count(i)]=i

    return medical_speciality[count[max(count.keys())]]

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)