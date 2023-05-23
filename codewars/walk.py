#You live in the city of Cartesia where all roads are laid out in a perfect grid.
#You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
#The city provides its citizens with a Walk Generating App on their phones -- every time you press the button, it sends you an array of one-letter strings representing directions to walk (e.g., ['n', 's', 'w', 'e']).
#You always walk only a single block for each letter (direction), and you know it takes you one minute to traverse one city block. Therefore, create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point.
#Return false otherwise.

def is_valid_walk(walk):
    total = [0, 0]
    time = 0
    
    for i in walk:
        time += 1
        if i == 'n':
            total[1] += 1
        elif i == 's':
            total[1] -= 1
        elif i == 'e':
            total[0] += 1
        else:
            total[0] -= 1
    
    return (time == 10) and (total == [0, 0])
    