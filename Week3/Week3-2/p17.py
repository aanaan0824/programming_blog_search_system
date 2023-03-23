import re

a = "how are you"
print("\bare\b")
print("\bare\bare")
print(re.findall("\bare\b", a))
print(re.findall(r"\bare\b", a))
