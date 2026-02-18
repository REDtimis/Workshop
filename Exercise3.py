import sqlite3

# connect to database (creates file if not exists)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# insert 3 rows
cursor.execute("INSERT INTO students (name, age) VALUES ('Ahmed', 23)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Lina', 19)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Yacine', 25)")

conn.commit()

# select students older than 20
cursor.execute("SELECT * FROM students WHERE age > 20")
results = cursor.fetchall()

print("Students older than 20:")
for student in results:
    print(student)

conn.close()
