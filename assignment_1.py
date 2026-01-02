Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Marks1 = float(input("enter your first marks: "))
Marks2 = float(input("enter your second marks: "))
Marks3 = float(input("enter your third marks: "))
Total_Marks = Marks1 + Marks2 + Marks3
Average_Marks = Total_Marks / 3
if Average_Marks >=75:
    Grade = "A"
elif Average_Marks >=60:
    Grade = "B"
elif Average_Marks >=50:
    Grade = "C"
else:
    Grade = "F"
print("Name:", Name)
print("Age:", Age)
print("Total Marks:", Total_Marks)
print("Average Marks:", Average_Marks)
print("Grade:", Grade)
