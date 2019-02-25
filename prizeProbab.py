import random

prizes = ['Rs 1', 'Rs 2', 'Rs 5', 'Rs 10', 'Rs 20']
probability = [0.4, 0.3, 0.2, 0.1, 0.05]

# creates lst as 2d - list  for outcomes for a given probability


def win(prizes, probability):
    zipped = zip(prizes, probability)

    lst = [[i[0]] * int(i[1] * 100) for i in zipped]
    outcomes = [b for i in lst for b in i]
    return outcomes


# returns a list win_check
win_check = win(prizes, probability)
# random win selects a random Prize from win_check
randomWin = random.choices(win_check)
# convert list to string
print('You Won : '+''.join(randomWin))
