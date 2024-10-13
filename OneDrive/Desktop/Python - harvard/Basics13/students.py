# with open ("students.csv") as file:
#     for line in file:
#         name,house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
# import csv
# students = []

# with open("students.csv") as file:
#     # for line in file:
#     #    name,house =line.rstrip().split(",")
#     #    student = {"name" : name , "house" : house}
#     #    students.append(student)
#     reader = csv.reader(file)
#     for name,home in reader:
#             students.append({"name" : name , "home" : home})
# for student in sorted(students , key = lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

# import csv
# students = []

# with open("students.csv") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             students.append({"name" : row['name'] , "home" : row['home']})
    
# for student in sorted(students , key = lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")
        
        
import csv

students = []
name = input("What is your name? ")
home = input("House? ")

# Open the CSV file in append mode
with open("students.csv", "a", newline='') as file:
    # Specify the fieldnames
    fieldnames = ["name", "home"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # If the file is empty, write the header
    if file.tell() == 0:  # Check if the file is empty
        writer.writeheader()
    
    # Write the new student information
    writer.writerow({"name": name, "home": home})

print("Student information added successfully.")

