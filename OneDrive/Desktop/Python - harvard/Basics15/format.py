import re

name = input("Enter name: ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"  # Added space between first and last names

# print(f"Hello, {name}")  # Added space after "Hello,"
if matches:=re.search (r"^(.+), ?(.+)$" , name):
    name = matches.group(2) + " " + matches.group(1)
    
print(f"hello , {name}")