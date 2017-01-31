import pygame
from random import randint
from Node import Node
import copy
riv = []

def makePartialBlock(tmpGrid):
    for row in range(120):
        # Add an empty array that will hold each cell
        # in this row
        tmpGrid.append([])
        for column in range(160):
            tmpNode = Node()
            tmpGrid[row].append(tmpNode)  # Append a cell
    for i in range(0, 8):
        tmpRow = randint(0, 119)

        tmpCol = randint(0, 159)

        for a in range(tmpRow - 15, tmpRow + 16):
            if (a >= 120):
                tmpA = a
                a = tmpA - 120
            elif (a < 0):
                tmpA = a
                a = 120 + tmpA
            for b in range(tmpCol - 15, tmpCol + 16):
                if (b >= 160):
                    tmpB = b
                    b = tmpB - 160
                elif (b < 0):
                    tmpB = b
                    b = 160 + tmpB
                try:
                    willBlock = randint(0, 1)
                    if (willBlock == 1):
                        tmpGrid[a][b].block = True
                        tmpGrid[a][b].color = (211, 211, 211)
                except NameError:
                    pass

    return tmpGrid

def makeRiverIter(tmpMap):
    BMap=copy.deepcopy(tmpMap)
    CMap=copy.deepcopy(tmpMap)
    totCount=0
    counter=0
    appendRiv=[]
    while(counter<4):
        riv=[]
        toContinue=0
        dist=0
        side=randint(1,4) #4 sides, 1 is left, 2 is right, 3 is top, 4 is bot
        if(side==1):
            row=randint(0,119)
            col=0
            for i in range(0,21):
                if(BMap[row][col]==1):
                    toContinue=-1
                else:
                    BMap[row][col]=1
                    dist=dist+1
                    col=col+1
            which=0

            while (toContinue == 0):
                if (which == 0):
                        where = randint(1,
                                        10)  # if its 1-6, river goes in same dir. if 7/8, river goes up. if 9/10, river goes down.
                        if (where <= 6):
                            BMap, row, col, dist, toContinue, which = riverRight(BMap, row, col, dist)
                        elif (where <= 8):
                            BMap, row, col, dist, toContinue, which = riverUp(BMap, row, col, dist)
                        else:
                            BMap, row, col, dist, toContinue, which = riverDown(BMap, row, col, dist)
                elif (which == 1):
                        where = randint(1, 10)
                        if (where <= 6):
                            BMap, row, col, dist, toContinue, which = riverLeft(BMap, row, col, dist)
                        elif (where <= 8):
                            BMap, row, col, dist, toContinue, which = riverUp(BMap, row, col, dist)
                        else:
                            BMap, row, col, dist, toContinue, which = riverDown(BMap, row, col, dist)
                elif (which == 2):
                        where = randint(1, 10)
                        if (where <= 6):
                            BMap, row, col, dist, toContinue, which = riverUp(BMap, row, col, dist)
                        elif (where <= 8):
                            BMap, row, col, dist, toContinue, which = riverLeft(BMap, row, col, dist)
                        else:
                            BMap, row, col, dist, toContinue, which = riverRight(BMap, row, col, dist)
                else:
                        where = randint(1, 10)
                        if (where <= 6):
                            BMap, row, col, dist, toContinue, which = riverDown(BMap, row, col, dist)
                        elif (where <= 8):
                            BMap, row, col, dist, toContinue, which = riverLeft(BMap, row, col, dist)
                        else:
                            BMap, row, col, dist, toContinue, which = riverRight(BMap, row, col, dist)
            if(toContinue==1 and dist>=100):
                    counter+=1
                    CMap=copy.deepcopy(BMap)
            else:
                   # print "redo"
                    totCount+=1
                    BMap = copy.deepcopy(CMap)
                    riv = []
                    toContinue = 0
                    dist = 0
        elif(side==2):
            row=randint(0,119)
            col=159

            for i in range(0,21):
                if(BMap[row][col]==1):
                    toContinue=-1
                    break
                else:
                    BMap[row][col]=1
                    dist=dist+1
                    col=col-1
            which=1
            while (toContinue == 0):
                if (which == 0):
                        where = randint(1,
                                        10)  # if its 1-6, river goes in same dir. if 7/8, river goes up. if 9/10, river goes down.
                        if (where <= 6):
                            BMap, row, col, dist, toContinue, which = riverRight(BMap, row, col, dist)
                        elif (where <= 8):
                            BMap, row, col, dist, toContinue, which = riverUp(BMap, row, col, dist)
                        else:
                            BMap, row, col, dist, toContinue, which = riverDown(BMap, row, col, dist)
                elif (which == 1):
                        where = randint(1, 10)
                        if (where <= 6):
                            BMap, row, col, dist, toContinue, which = riverLeft(BMap, row, col, dist)
                        elif (where <= 8):
                            BMap, row, col, dist, toContinue, which = riverUp(BMap, row, col, dist)
                        else:
                            BMap, row, col, dist, toContinue, which = riverDown(BMap, row, col, dist)
                elif (which == 2):
                        where = randint(1, 10)
                        if (where <= 6):
                            BMap, row, col, dist, toContinue, which = riverUp(BMap, row, col, dist)
                        elif (where <= 8):
                            BMap, row, col, dist, toContinue, which = riverLeft(BMap, row, col, dist)
                        else:
                            BMap, row, col, dist, toContinue, which = riverRight(BMap, row, col, dist)
                else:
                        where = randint(1, 10)
                        if (where <= 6):
                            BMap, row, col, dist, toContinue, which = riverDown(BMap, row, col, dist)
                        elif (where <= 8):
                            BMap, row, col, dist, toContinue, which = riverLeft(BMap, row, col, dist)
                        else:
                            BMap, row, col, dist, toContinue, which = riverRight(BMap, row, col, dist)
            if(toContinue==1 and dist>=100):
                    counter+=1
                    CMap=copy.deepcopy(BMap)
            else:
                    totCount+=1
                    BMap = copy.deepcopy(CMap)
                    riv = []
                    toContinue = 0
                    dist = 0
        elif(side == 3):
            col = randint(0, 159)
            row = 0

            for i in range(0,21):
                if(BMap[row][col]==1):
                    toContinue=-1
                else:
                    BMap[row][col]=1
                    dist=dist+1
                    row=row+1
            which = 3
            while (toContinue == 0):

                if (which == 0):
                    where = randint(1,
                                    10)  # if its 1-6, river goes in same dir. if 7/8, river goes up. if 9/10, river goes down.
                    if (where <= 6):
                        BMap, row, col, dist, toContinue, which = riverRight(BMap, row, col, dist)
                    elif (where <= 8):
                        BMap, row, col, dist, toContinue, which = riverUp(BMap, row, col, dist)
                    else:
                        BMap, row, col, dist, toContinue, which = riverDown(BMap, row, col, dist)
                elif (which == 1):
                    where = randint(1, 10)
                    if (where <= 6):
                        BMap, row, col, dist, toContinue, which = riverLeft(BMap, row, col, dist)
                    elif (where <= 8):
                        BMap, row, col, dist, toContinue, which = riverUp(BMap, row, col, dist)
                    else:
                        BMap, row, col, dist, toContinue, which = riverDown(BMap, row, col, dist)
                elif (which == 2):
                    where = randint(1, 10)
                    if (where <= 6):
                        BMap, row, col, dist, toContinue, which = riverUp(BMap, row, col, dist)
                    elif (where <= 8):
                        BMap, row, col, dist, toContinue, which = riverLeft(BMap, row, col, dist)
                    else:
                        BMap, row, col, dist, toContinue, which = riverRight(BMap, row, col, dist)
                else:
                    where = randint(1, 10)
                    if (where <= 6):
                        BMap, row, col, dist, toContinue, which = riverDown(BMap, row, col, dist)
                    elif (where <= 8):
                        BMap, row, col, dist, toContinue, which = riverLeft(BMap, row, col, dist)
                    else:
                        BMap, row, col, dist, toContinue, which = riverRight(BMap, row, col, dist)
            if (toContinue == 1 and dist >= 100):
                counter += 1
                CMap = copy.deepcopy(BMap)
            else:
                print "redo"
                totCount += 1
                BMap = copy.deepcopy(CMap)
                riv = []
                toContinue = 0
                dist = 0
        else:
           # print "side 4"
           # print counter
            col = randint(0, 119)
            row = 119
            for i in range(0,21):
                if(BMap[row][col]==1):
                    toContinue=-1
                else:
                    BMap[row][col]=1
                    dist=dist+1
                    row=row-1
            which = 2
            while (toContinue == 0):

                if (which == 0):
                    where = randint(1,
                                    10)  # if its 1-6, river goes in same dir. if 7/8, river goes up. if 9/10, river goes down.
                    if (where <= 6):
                        BMap, row, col, dist, toContinue, which = riverRight(BMap, row, col, dist)
                    elif (where <= 8):
                        BMap, row, col, dist, toContinue, which = riverUp(BMap, row, col, dist)
                    else:
                        BMap, row, col, dist, toContinue, which = riverDown(BMap, row, col, dist)
                elif (which == 1):
                    where = randint(1, 10)
                    if (where <= 6):
                        BMap, row, col, dist, toContinue, which = riverLeft(BMap, row, col, dist)
                    elif (where <= 8):
                        BMap, row, col, dist, toContinue, which = riverUp(BMap, row, col, dist)
                    else:
                        BMap, row, col, dist, toContinue, which = riverDown(BMap, row, col, dist)
                elif (which == 2):
                    where = randint(1, 10)
                    if (where <= 6):
                        BMap, row, col, dist, toContinue, which = riverUp(BMap, row, col, dist)
                    elif (where <= 8):
                        BMap, row, col, dist, toContinue, which = riverLeft(BMap, row, col, dist)
                    else:
                        BMap, row, col, dist, toContinue, which = riverRight(BMap, row, col, dist)
                else:
                    where = randint(1, 10)
                    if (where <= 6):
                        BMap, row, col, dist, toContinue, which = riverDown(BMap, row, col, dist)
                    elif (where <= 8):
                        BMap, row, col, dist, toContinue, which = riverLeft(BMap, row, col, dist)
                    else:
                        BMap, row, col, dist, toContinue, which = riverRight(BMap, row, col, dist)
            if (toContinue == 1 and dist >= 100):
                counter += 1
                CMap = copy.deepcopy(BMap)
            else:
                #print "redo"
                totCount += 1
                BMap = copy.deepcopy(CMap)
                riv = []
                toContinue = 0
                dist = 0
        if (totCount>25):
            #print "REDOING IT"
            BMap = copy.deepcopy(tmpMap)
            totCount = 0
            counter = 0
            appendRiv = []
            riv=[]
            map=[]
            dist=0
    return BMap


def riverRight(map, row, col, dist):
    cont = 0
    for i in range(0, 21):
        try:
            col = col + 1
            if (map[row][col]==0):
                map[row][col] = 1
                dist = dist + 1
                if (col >= 159):
                    cont = 1
                    map[row][159]=1
                    break

            else:
                cont = -1
                return map, row, col, dist, cont, 0
        except IndexError:
            return map, row, col, dist, cont, 0
    return map, row, col, dist, cont, 0


def riverLeft(map, row, col, dist):
    cont = 0
    for i in range(0, 21):
        try:
            col = col - 1
            if (map[row][col] ==0):
                map[row][col] = 1
                dist = dist + 1
                if (col <= 0):
                    map[row][0]=1
                    cont = 1
                    break
            else:
                cont = -1
                return map, row, col, dist, cont, 1
        except IndexError:
            return map, row, col, dist, cont, 1
    return map, row, col, dist, cont, 1


def riverUp(map, row, col, dist):
    cont = 0
    for i in range(0, 21):
        try:
            row = row - 1
            if (map[row][col] == 0):
                map[row][col] = 1
                dist = dist + 1
                if (row <= 0):
                    map[0][col]=1
                    cont = 1
                    break

            else:
                cont = -1
                return map, row, col, dist, cont, 2
        except IndexError:
            return map,row,col,dist,cont,2
    return map, row, col, dist, cont, 2


def riverDown(map, row, col, dist):
    cont = 0
    for i in range(0, 21):
        try:
            row = row + 1
            if (map[row][col] == 0):
                map[row][col] = 1
                dist = dist + 1
                if (row >= 119):
                    map[119][col]=1
                    cont = 1
                    break
            else:
                cont = -1
                return map, row, col, dist, cont, 3
        except IndexError:
            return map,row,col,dist,cont,3
    return map, row, col, dist, cont, 3


'''
def insertFile(file):
    grid=[]
    file_obj=open(file,'r')
    start=file_obj.readline(1)
    firstrownum=start.index(',')
    firstrow=start[:firstrownum]
    firstcol=start[firstrownum+1:]
    secondLine=file_obj.readline(2)
    secondrownum=secondLine.index(',')
    secondrow=secondLine[:secondrownum]
    secondcol=secondLine[secondrownum+1:]
    for row in range(120):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(160):
            tmpNode = Node()
            grid[row].append(tmpNode)  # Append a cell

    for i in range(120):
        tmp=file_obj.readline(i+11)
        for num in range(160):
            if(tmp[num]==0):
                grid[i][num].color=(0,0,0)
            elif(tmp[num]==1)
'''


def texts():
    font = pygame.font.Font(None, 30)
    scoretext = font.render("Score:", 1, (0, 255, 0))
    screen.blit(scoretext, (1150, 100))


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
makePartialBlock(grid)
# Initialize pygame
pygame.init()
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1250, 722]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Civ V Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 6
HEIGHT = 5
# This sets the margin between each cell
MARGIN = 1
rivcount=0

stuff=[]

for row in range(120):
        # Add an empty array that will hold each cell
        # in this row
    stuff.append([])
    for column in range(160):
        stuff[row].append(0)  # Append a cell


stuff1=makeRiverIter(stuff)

counter=0
while(counter<3840):
    row=randint(0,119)
    col=randint(0,159)
    if(stuff1[row][col]==0):
        stuff1[row][col]=2
        counter+=1

for row in range(120):
    for column in range(160):
        color = grid[row][column].color
        if stuff1[row][column] == 1:
            grid[row][column].color=(0,0,255)
        elif(stuff1[row][column]==2):
            grid[row][column].color=(0,0,0)
        grid[row][column].topLeft = ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN)
        grid[row][column].centerTop = ((MARGIN + WIDTH) * column + MARGIN + 3, (MARGIN + HEIGHT) * row + MARGIN)
        grid[row][column].centerLeft = ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN + 2.5)
        grid[row][column].centerRight = (
            (MARGIN + WIDTH) * column + MARGIN + 6, (MARGIN + HEIGHT) * row + MARGIN + 2.5)
        grid[row][column].centerBot = ((MARGIN + WIDTH) * column + MARGIN + 3, (MARGIN + HEIGHT) * row + MARGIN + 5)


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            try:
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                grid[row][column].color = (0, 150, 255)
                print("Click ", pos, "Grid coordinates: ", row, column)
            except IndexError:
                print("Hey dont click there")

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(120):
        for column in range(160):
            color = grid[row][column].color
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)
    #pygame.draw.lines(screen,(0,0,255),False,stuff[0],1)
    #pygame.draw.lines(screen,(0,0,255),False,stuff[1],1)
    #pygame.draw.lines(screen,(0,0,255),False,stuff[2],1)
    #pygame.draw.lines(screen,(0,0,255),False,stuff[3],1)

    # Go ahead and update the screen with what we've drawn.
    # list = [grid[50][0].centerLeft, grid[50][100].centerLeft]






    #if (rivcount > 0):
        #pygame.draw.lines(screen, (0, 0, 255), False, riv[0], 1)
        #pygame.draw.lines(screen, (0, 0, 255), False, riv[1], 1)
        #pygame.draw.lines(screen, (0, 0, 255), False, riv[2], 1)
        #pygame.draw.lines(screen, (0, 0, 255), False, rivD, 1)

    texts()

    pygame.display.flip()


# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
