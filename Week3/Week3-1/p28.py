import re
print ("\ahow are you")
print ("how \bare\b you")
print (r"how \bare\b you")

a = "how are you"
print("1")
print(re.findall(r"\bare\b", a))
print("2")
print(re.findall("\bare\b", a))
