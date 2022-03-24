num1 = int(input("Enter a First interval number : "))
num2 = int(input("Enter a last interval number : "))
odd_num = 0
even_num = 0
for i in range(num1, num2):
    if not i % 2:
        even_num += 1
    else:
        odd_num += 1
print("Number of even numbers : ", even_num)
print("Number of odd numbers : ", odd_num)