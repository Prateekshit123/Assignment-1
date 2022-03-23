num = int(input("Please enter a range number: "))
First_num = 0
Second_num = 1
if num <= 0:
       print("Please enter a Positive number")
else:
    print(First_num)
    print(Second_num)
for i in range(2, num):
        next = First_num + Second_num
        First_num = Second_num
        
        Second_num = next
        if next <= num:
            print(next)