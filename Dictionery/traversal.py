students = { "name":"Alice", "age":20, "course":"Computer Science" }
print(students)

        #return value one by one
for key in students:
    print(students[key])

for i,j in students.items():
    print(f"Key: {i}, Value: {j}")

