print("Abdus Samad Chowhan UIN:251P126")

students={
    101:{"Name":"Abdus Samad","Grade":"A","Attendence":90},
    102:{"Name":"Omkar","Grade":"B","Attendence":85},
    103:{"Name":"Zaid","Grade":"A","Attendence":95}
}

students[104]={"Name":"Zoheb","Grade":"B","Attendence":80}

print(students)

students[101]["Grade"]="A+"

print(students)

for student_id,details in students.items():
    print(f"ID:{student_id},Name:{details['Name']},Grade:{details['Grade']},Attendence:{details['Attendence']}%")
    print(students.keys())
    print(students.values())
    print(students.items())