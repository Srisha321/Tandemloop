a = int(input("Enter a number: "))
odd_number = 1
for i in range(a):
    if i == a - 1:
        print(odd_number)
    else:
        print(odd_number, end=", ")
    odd_number += 2
