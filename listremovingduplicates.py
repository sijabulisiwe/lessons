#x=[1,2,4,4,5,6,6,8,9]
#x =list(dict.fromkeys(x))
#print(x)
students = ['Python', 'R', 'C#', 'Python', 'R', 'Java']

new_list = []

for one_student_choice in students:
    if one_student_choice not in new_list:
        new_list.append(one_student_choice)

print(new_list)


    
    
    
    