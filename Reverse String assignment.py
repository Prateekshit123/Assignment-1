string = input("Please enter a String : ")
str = ''
for i in string:
    str = i + str
print("\nThe Original String : ", string)
print("The Reversed String : ", str)