# Script for building shortcuts for remote connection in network
# Set number of files in range, add data in file content as needed

for number in range(1, 4):
    padded_number = f"{number:04}"
    filename = f"testname{padded_number}.txt"
    content = f"number: {padded_number}\nline 2\nline 3\nSome data: data\nAnother data: can you imagine"
    
    with open(filename, "w") as file:
        file.write(content)

print("Files created.")