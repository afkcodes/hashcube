patternLen = int(input('Enter Pattern length: '))

for i in range(0, patternLen):
    print(' ' * (patternLen - i) + '* ' * i)
