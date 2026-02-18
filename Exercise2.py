# write to TXT file
with open("example.txt", "w") as file:
    file.write("Hello PhD Students\n")
    file.write("Python Programming Workshop\n")

# read TXT file
with open("example.txt", "r") as file:
    content = file.read()
    print("TXT File Content:")
    print(content)
    
import csv

# Write CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Ali", 25])
    writer.writerow(["Sara", 22])

# Read CSV file
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    print("CSV File Content:")
    for row in reader:
        print(row)
