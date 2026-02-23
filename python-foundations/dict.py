#creation 
student = {
    'name' : 'Sher Bdr' ,
    'age' : 78,
    'roll': 23,
}


#accessing
print(student.get('name', 'not found'))


#updaiting
student['name'] = 'Bhesh Bahadur Saru'

student['age'] = 52 
student['contact'] = 981646816 

print(student)


# del student['name']
# print(student.pop('age'))
print (dir( student))

# for _,values in student.items():
#     print(values)

    # for i in student.items():
    #     print(i)

# for i in student.items():
#     print(i)

print (type( student . keys( ) ) )
print (type( student. values( ) ) )
print (type( student. items( ) ) )