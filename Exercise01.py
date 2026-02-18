# Exercise 1
numbers = [1, 2, 3, 4, 5]

# find minimum using for-loop
min_value = numbers[0]

for num in numbers:
    if num < min_value:
        min_value = num

print("Minimum value:", min_value)


# show even numbers
print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)


# replace even numbers by 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = 0

print("Modified list:", numbers)
