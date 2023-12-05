numbers_ = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
t = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}


with open("day1.txt", 'r') as plik:
    sum_ = 0
    for line in plik.read().split("\n"):
        numbers = ""
        for index, letter in enumerate(line):
            if letter.isdigit():
                numbers += letter
            else:
                for key, value in t.items():
                    if line[index:].startswith(value):
                        numbers += key
        if len(numbers) > 1:
            sum_ += int(numbers[0] + numbers[-1])
        else:
            sum_ += int(numbers[0] + numbers[0])
        
print(sum_)