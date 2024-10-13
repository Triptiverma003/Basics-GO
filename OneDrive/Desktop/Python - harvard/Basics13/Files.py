#name = []

# with open ("names.txt" ,"w") as file:
#     file.write(f"{name}\n")

# with open ("names.txt" , "r") as file:
#    for line in file:
#        print("hello" , line.rstrip())

with open("names.txt" , "r") as file:
    for line in sorted(file , reverse = "true"):
        print("hello" , line.rstrip())
        