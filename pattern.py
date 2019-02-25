patternLen = int(input('Enter Pattern length: '))

for i in range(0, patternLen):
	# Generate Spaces and Corresponding star Pattern
    print(' ' * (patternLen - i) + '* ' * i)
