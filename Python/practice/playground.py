import re

str = "   +123 a"

#Check if the string contains "a" followed by exactly two "l" characters:

x = re.search(r'[+\-]?\d+', str)

print(x)
print(type(int(x.group())))

if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")
