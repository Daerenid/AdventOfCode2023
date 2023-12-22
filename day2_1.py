with open("day2.txt", 'r') as plik:
    sum_ = 0
    for index, game in enumerate(plik.read().split("\n"), start=1):
        errors = 0
        index_ = game.index(":")
        for subsets in game[index_+2:].split("; "):
            for subset in subsets.split(", "):
                space = subset.index(" ")
                number = subset[:space]
                color = subset[space+1:]
                if color == "green" and int(number) > 13:
                    errors += 1
                if color == "red" and int(number) > 12:
                    errors +=1
                if color == "blue" and int(number) > 14:
                    errors += 1
        if errors == 0:
            sum_ += index               

print(sum_)