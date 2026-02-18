class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


# Example usage
student1 = Student("Karim", 24, [15, 14, 16, 18])

print("Name:", student1.name)
print("Age:", student1.age)
print("Average grade:", student1.average())
