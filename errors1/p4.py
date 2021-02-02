# The goal of this program is to print the product of the list of numbers.
values = []
for i in range(5):
    num = int(input("Enter a number: "))
    values.append(num)
result = 0
for number in values:
    result *= number
print(result)
