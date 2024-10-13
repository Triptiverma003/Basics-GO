# email = input("'what is your email?:").strip()

# if "@" in email:
#     print("valid")

# else:
#     print("invalid")

import re

email = input("what is your email: ?")

if re.search( r"^\w.+@\w.+\.edu$" , email , re.IGNORECASE):
    print("valid")

else:
    print("invalid")
    
# here re.search( pattern , parameter , flags)
#flags jo ki use ho sakte hai woh hai:->
# re.IGNORECASE . re.MULTILINE , re.DOTALL
# if i want to introduce specifically .edu...mai bas ./edu laga dungi
# isse yh hoga ki mai specifically edu ko hee define kr dungi

#python mei ^ use hota hai ki mera expressions ke aage wala match kre.
#aur $ use hota hai so that mere expressions ke last wale string match kre.

#[^a] use hota hai so that we can compliment the string.

#[] set of character

#[] ismein set of character numbers ka use ho sakta hai...

#here \w use hota hai words ke liye.


#re.match(patterns , parameter , flag)