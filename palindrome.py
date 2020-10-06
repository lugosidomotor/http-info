def palindrome(input):
    length = len(input)
    palindromes = []
    for i in range(1,length+1):
        min = 0
        while (min+i) < length+1:
            print(input[min:(min+i)])
            if(input[min:(min+i)] == input[min:(min+i)][::-1]) and len(input[min:(min+i)]) >= 3:
                palindromes.append(input[min:(min+i)])
            min = min+1
    return palindromes

print(palindrome("dog goat dad duck doodle never"))
print(palindrome("racecar"))
