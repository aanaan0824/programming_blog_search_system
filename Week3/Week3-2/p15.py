import re

print(re.match(r"a.*b", "baabab"))
print(re.match(r"a.*?b", "aabab"))
print(re.findall(r"a.*?b", "aabab"))

