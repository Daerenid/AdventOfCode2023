with open("day2.txt", 'r') as plik:
    sum_ = 0
    for index, game in enumerate(plik.read().split("\n"), start=1):
        red = []
        blue = []
        green = []
        index_ = game.index(":")
        for subsets in game[index_+2:].split("; "):
            for subset in subsets.split(", "):
                space = subset.index(" ")
                number = subset[:space]
                color = subset[space+1:]
                if color == "green":
                    green.append(int(number))
                if color == "red":
                    red.append(int(number))
                if color == "blue":
                    blue.append(int(number))
        sum_ += (max(red)*max(blue)*max(green))
print(sum_)