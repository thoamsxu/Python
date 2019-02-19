# while 循环
numbers = input("please input numbers, user ','").split(",")
print(numbers)
x = 0
while x < len(numbers):
    print(numbers[x])
    x = x + 1