import re

url = input("URL: ").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
else:
    print("Invalid Twitter URL.")

# username = re.sub(r"https?://twitter\.com/", "", url)
# print(f"username : {username}")

#username = url.replace("https://twitter.com/", "")
#print(f"Username: {username}")
#replace function is used to remove the replace the variable with another.
#variable.remove("the variable you are removing" , "the variable you are removing with")