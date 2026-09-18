dog={}

dog={"Name":"","Age":"","Breed":"","Color":"","Legs":""}

student={"first_name":"","last_name":"","gender":"","age":"","martial_status":"","skills":["skill1"],
         "country":"","city":"","adresse":""}
print(len(student))
print(student["skills"])
print(type(student["skills"]))
student["skills"].append("skill2")
student["skills"].append("skills3")
print(student["skills"])
student_keys_list=list(student.keys())
print(student_keys_list)
student_values_list=list(student.values())
print(student_values_list)
student_tuple=student.items()
print(student_tuple)
del student["age"]
print(student.get("age"))
del student
