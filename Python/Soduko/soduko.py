tiles = [[0]*9]*9

for i in range(9):
    tiles[i] = int(input().split())


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
   


printTiles()




