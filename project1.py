import pygame
from random import randint
from Node import Node

def generateMap(tmpGrid):
    makePartialBlock(tmpGrid)


def makePartialBlock(tmpGrid):
    for row in range(120):
        # Add an empty array that will hold each cell
        # in this row
        tmpGrid.append([])
        for column in range(160):
            tmpNode = Node()
            tmpGrid[row].append(tmpNode)  # Append a cell
    for i in range(0,8):
        tmpRow=randint(0,119)

        tmpCol=randint(0,159)

        for a in range(tmpRow-15,tmpRow+16):
            if(a>=120):
                tmpA=a
                a=tmpA-120
            elif(a<0):
                tmpA=a
                a=120+tmpA
            for b in range(tmpCol-15,tmpCol+16):
                if(b>=160):
                    tmpB=b
                    b=tmpB-160
                elif(b<0):
                    tmpB=b
                    b=160+tmpB
                try:
                    willBlock=randint(0,1)
                    if(willBlock==1):
                        tmpGrid[a][b].block=True
                        tmpGrid[a][b].color=(211,211,211)
                except NameError:
                    pass


    return tmpGrid

def makeRiver(tmpGrid):
    BGrid = list(tmpGrid)
    for i in range(0,4):
        side=randint(1,4)#there are 4 sides on the grid, so decides which side to start on. 1 will be left, 2 will be right, 3 will be top, 4 will be bot
        if(side==1 or side==2):
            pos=randint(0,119)
            if(side==1):
                dir=randint(0,1)#decides whether to move vertical or horizontally, 0 = horiz and 1 = vert
                if(dir==0):
                    pass
            else:
                pass
        else:
            pos=randint(0,159)
            if(side==3):
                pass
            else:
                pass

def texts():
   font=pygame.font.Font(None,30)
   scoretext=font.render("Score:", 1,(0,255,0))
   screen.blit(scoretext, (1150, 100))


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
generateMap(grid)
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
                grid[row][column].color=(0,150,255)
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
            pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
            grid[row][column].topLeft=((MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN)
            grid[row][column].centerLeft=((MARGIN + WIDTH) * column + MARGIN + 2.5,(MARGIN + HEIGHT) * row + MARGIN)
            grid[]

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    #list = [grid[0][0].topLeft, grid[100][100].topLeft]

    #pygame.draw.lines(screen,(255,0,0),True,list,1)
    texts()

    pygame.display.flip()



# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()