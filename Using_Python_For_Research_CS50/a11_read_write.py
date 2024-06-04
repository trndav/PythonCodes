'''
Checking mem leaks with pylint
'''

# Read file
FILE = "somefile.txt"

for line in open(FILE, encoding='utf-8'):
    strip = line.strip()
    print(strip)

with open(FILE, encoding='utf-8') as f:
    for line in f:
        rstrip = line.rstrip()
        print(rstrip.split(" "))


# Write file
F = open("output.txt", "w", encoding='utf-8')
F.write("Python is the \nbest!\n")
F.close()
lines = []
for line in open("output.txt"):
    lines.append(line.strip())
print(lines)

# with open("output.txt", "a", encoding='utf-8') as file:
#     file.write("Panic!\n")
