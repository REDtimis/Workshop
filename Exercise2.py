# write to TXT file
with open("example.txt", "w") as file:
    file.write("Hello PhD Students\n")
    file.write("Python Programming Workshop\n")

# read TXT file
with open("example.txt", "r") as file:
    content = file.read()
    print("TXT File Content:")
    print(content)
