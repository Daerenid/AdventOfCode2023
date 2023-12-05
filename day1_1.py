with open("day1.txt", 'r') as plik:
    sum_ = 0
    for line in plik.read().split("\n"):
        numbers = ""
        for letter in line:
            if letter.isnumeric():
                numbers += letter
        if len(numbers) > 1:
            number = numbers[0] + numbers[-1]
        else:
            number = numbers[0] + numbers[0]
        sum_ += int(number)
    
print(sum_)