def find_max(numbers):
    maxim = numbers[0]
    for x in numbers:
        if x > maxim:
            maxim = x
    
    return maxim

