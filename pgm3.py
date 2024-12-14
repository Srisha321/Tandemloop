numbers = input("Enter numbers separated by space: ").split()
numbers = [int(num) for num in numbers]

count_dict = {i: 0 for i in range(numbers)}

for num in numbers:
    for i in range(1, 10):
        if num % i == 0:
            count_dict[i] += 1

print(count_dict)
