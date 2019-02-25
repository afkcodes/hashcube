import random

prizes = ['Rs 1', 'Rs 2', 'Rs 5', 'Rs 10', 'Rs 20']
probability = [0.4, 0.3, 0.2, 0.1, 0.05]


def win(prizes, probability):
    zipped = zip(prizes, probability)

    lst = [[i[0]] * int(i[1] * 100) for i in zipped]
    outcomes = [b for i in lst for b in i]
    return outcomes


win_check = win(prizes, probability)
randomWin = random.choices(win_check)
print(''.join(randomWin))
