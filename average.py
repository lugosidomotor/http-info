numbers = [1, 2, 3, 4, 5]

def average(list):
    sum = 0
    for i in range(len(list) + 1):
        sum += i
    return sum/len(list)

print(average(numbers))
