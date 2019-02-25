# import random
# sudoku = []
# for i in range(0, 9):
#     sudoku.append([])
#     for j in range(0, 9):
#         sudoku[i].append(random.randrange(1, 10))
sudoku = [
    [2, 7, 5, 1, 9, 8, 3, 6, 4],
    [1, 4, 3, 5, 7, 6, 9, 2, 8],
    [8, 9, 6, 2, 4, 3, 1, 7, 5],
    [3, 2, 8, '', 6, 1, 7, 5, 9],
    [4, 5, 7, 9, 8, 2, 6, 1, 3],
    [6, 1, 9, 7, 3, 5, 4, 8, 2],
    [7, 8, 1, 3, 2, 4, 5, 9, 6],
    [5, 3, 2, 6, 1, 9, 8, 4, 7],
    [9, 6, 4, 8, 5, 7, 2, 3, 1]
]

print('SUDOKU')
print('\n \n')

for mat in sudoku:
    print(mat)


def checkSudoku(sudoku):
    if checkRows(sudoku, xPos) == True:
        if checkCols(sudoku, yPos) == True:
            if checkBlocks(sudoku, blockId) == True:
                return True
    return False

# Check For valid Rows


def checkRows(rows, xPos):
    checknum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(rows[xPos])
    for num in checknum:
        if num not in rows[xPos]:
            return False
    return True


# Check For valid Rows

def checkCols(sudokuCols, yPos):
    opsudoku = list(map(list, zip(*sudokuCols)))
    return checkRows(opsudoku, yPos)


# Block values to List

def checkBlocks(blockVal, blockId):
    # print(xPos)
    allBox = []
    for i in range(0, 3):
        for j in range(0, 3):
            box = []
            val2 = 0
            for ii in range(0, 3):
                for jj in range(0, 3):
                    row = (3 * i) + ii
                    col = (3 * j) + jj
                    val = blockVal[row][col]
                    val2 = val
                    box.append(val2)
            allBox.append(box)
    return checkRows(allBox, blockId)


# Select Blocks

def selectBlock(xPos, yPos):
    if xPos >= 6 and yPos <= 2:
        blockSel = 6
    elif xPos >= 6 and yPos <= 5:
        blockSel = 7
    else:
        blockSel = 8

    if 2 < xPos <= 3 and yPos <= 2:
        blockSel = 3
    elif 2 < xPos < 6 and yPos <= 5:
        blockSel = 4
    elif 2 < xPos < 6:
        blockSel = 5

    if xPos <= 2 and yPos <= 2:
        blockSel = 0
    elif xPos <= 2 and yPos <= 5:
        blockSel = 1
    else:
        blockSel = 2

    return blockSel

# List of Valid Input & Ranges


validInput = [1, 2, 3, 4, 5, 6, 7, 8, 9]
validRange = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print('\n \n')

# Input for X and Y axis
xPos = int(input('Enter X [0-8] : '))
yPos = int(input('Enter Y [0-8] : '))

blockSel = 0
if xPos in validRange and yPos in validRange:
    # Get BlockID
    blockId = selectBlock(xPos, yPos)
    defaultValue = sudoku[xPos][yPos]
    # print(sudoku[xPos][yPos])
# handle the blank Values
    testVal = input('Enter Value : ')
    if testVal == '':
        testVal = ''
    else:
        testVal = int(testVal)
        sudoku[xPos][yPos] = testVal
#Check Existing with entered value
    if defaultValue == testVal and checkSudoku(sudoku) == True:
        print('"Valid Positon / Entry"')
    # print(checkRows(sudoku, xPos))
    # print(checkCols(sudoku, yPos))

    elif testVal in validInput:
        sudoku[xPos][yPos] = testVal
        if checkSudoku(sudoku) == True:
            print('Valid Positon / Entry')
        else:
            print('Invalid Position / Entry')
    else:
        print('Please Input Values between 1-9')
else:
    print('Invalid Axes Values')
