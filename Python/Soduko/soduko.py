tiles = [[0]*9]*9

allNums = set([1,2,3,4,5,6,7,8,9])
solved = False

for i in range(9):
    tiles[i] = list(map(int, input().split())) 


def printTiles():
    countY = 0
    print('─────────────────────────')
    for y in tiles:
        countX = 0
        print('|', end = ' ')
        for x in y:
            if(x != 0):
                print(x, end = ' ')
            else:
                print(' ', end = ' ')
            countX += 1
            if(countX % 3 == 0):
                print('|', end = ' ')
        print('')
        countY += 1
        if(countY % 3 == 0):
            print('─────────────────────────')
   

def get_square(y,x):
    xsqr = x // 3
    ysqr = y // 3
    sqr = set()
    for i in range(ysqr*3,ysqr*3+3):
        for j in range(xsqr*3,xsqr*3+3):
            sqr.add(tiles[i][j])
    return sqr

def get_hline(y):
    hline = set()
    for i in tiles[y]:
        hline.add(i)
    return hline

def get_vline(x):
    vline = set()
    for i in range(9):
        vline.add(tiles[i][x])
    return vline



def processTile(y,x):
    if(tiles[y][x] == 0):
        used = get_hline(y) | get_vline(x) | get_square(y,x)
        available = allNums - used
        if(len(available) == 1):
           tiles[y][x] = list(available)[0]




while(not solved):
    solved = True
    printTiles()
    for y in range(9):
        for x in range(9):
            processTile(y,x)
            if(tiles[y][x] == 0):
                solved = False

printTiles()
    





