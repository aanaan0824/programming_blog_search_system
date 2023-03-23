import re

a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")
print(a.match("2.345abc"))
print(b.match("2.345abc"))

print(re.match("^\d+$", "123\n 234\n"))
