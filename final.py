import pygame
from search import *
from random import randint
from Node import Node
import copy
import math
import time
riv = []
from memprof import *
def connectTheDots():
    for row in range(120):

        for column in range(160):
            tmp = grid[row][column]
            tmp.x = row
            tmp.y = column
            if (column + 1 < 160 and stuff1[row][column] != 2 and stuff1[row][column + 1] != 2):
                tmp.neighbor1 = grid[row][column + 1]
                if (stuff1[row][column + 1] == 1 and stuff1[row][column] == 1):
                    tmp.neighbor1Cost = 0.25
                elif(stuff1[row][column + 1] == 3 and stuff1[row][column] == 3 or stuff1[row][column + 1] == 4 and stuff1[row][column] == 3 or stuff1[row][column + 1] == 3 and stuff1[row][column] == 4):
                    tmp.neighbor1Cost = 2
                elif(stuff1[row][column + 1] == 4 and stuff1[row][column] == 4):
                    tmp.neighbor1Cost = 0.5
                elif(stuff1[row][column + 1] == 4 and stuff1[row][column] == 1 or stuff1[row][column + 1] == 1 and stuff1[row][column] == 4):
                    tmp.neighbor1Cost = 0.375
                elif(stuff1[row][column + 1] == 3 or stuff1[row][column]==3):
                    tmp.neighbor1Cost = 1.5
                else:
                    tmp.neighbor1Cost = 0.5
            if (row - 1 >= 0 and column + 1 < 160 and stuff1[row][column] != 2 and stuff1[row - 1][column + 1] != 2):
                tmp.neighbor2 = grid[row - 1][column + 1]
                if (stuff1[row-1][column + 1] == 1 and stuff1[row][column] == 1 ):
                    tmp.neighbor2Cost = 0.35
                elif (stuff1[row-1][column + 1] == 3 and stuff1[row][column] == 3 or stuff1[row-1][column + 1] == 4 and stuff1[row][column] == 3 or stuff1[row-1][column + 1] == 3 and stuff1[row][column] == 4):
                    tmp.neighbor2Cost = math.sqrt(8)
                elif (stuff1[row-1][column + 1] == 4 and stuff1[row][column] == 4):
                    tmp.neighbor2Cost = math.sqrt(2)
                elif (stuff1[row-1][column + 1] == 4 and stuff1[row][column] == 1 or stuff1[row-1][column + 1] == 1 and
                        stuff1[row][column] == 4):
                    tmp.neighbor2Cost = (3*math.sqrt(2))/8
                elif (stuff1[row-1][column + 1] == 3 or stuff1[row][column] == 3):
                    tmp.neighbor2Cost = (3*math.sqrt(2))/2
                else:
                    tmp.neighbor2Cost = 0.7

            if (row - 1 >= 0 and stuff1[row][column] != 2 and stuff1[row - 1][column] != 2):
                tmp.neighbor3 = grid[row - 1][column]
                if (stuff1[row-1][column] == 1 and stuff1[row][column] == 1):
                    tmp.neighbor3Cost = 0.25
                elif (stuff1[row-1][column] == 3 and stuff1[row][column] == 3 or stuff1[row-1][column] == 4 and stuff1[row][column] == 3 or stuff1[row-1][column] == 3 and stuff1[row][column] == 4):
                    tmp.neighbor3Cost = 2
                elif (stuff1[row-1][column] == 4 and stuff1[row][column] == 4):
                    tmp.neighbor3Cost = 0.5
                elif (stuff1[row-1][column] == 4 and stuff1[row][column] == 1 or stuff1[row-1][column] == 1 and stuff1[row][column] == 4):
                    tmp.neighbor3Cost = 0.375
                elif (stuff1[row-1][column] == 3 or stuff1[row][column] == 3):
                    tmp.neighbor3Cost = 1.5
                else:
                    tmp.neighbor3Cost = 0.5
            if (row - 1 >= 0 and column - 1 >= 0 and stuff1[row][column] != 2 and stuff1[row - 1][column - 1] != 2):
                tmp.neighbor4 = grid[row - 1][column - 1]
                if (stuff1[row-1][column - 1] == 1 and stuff1[row][column] == 1):
                    tmp.neighbor4Cost = 0.35
                elif (stuff1[row-1][column -1] == 3 and stuff1[row][column] == 3 or stuff1[row-1][column -1] == 4 and stuff1[row][column] == 3 or stuff1[row-1][column - 1] == 3 and stuff1[row][column] == 4):
                    tmp.neighbor4Cost = math.sqrt(8)
                elif (stuff1[row-1][column - 1] == 4 and stuff1[row][column] == 4):
                    tmp.neighbor4Cost = math.sqrt(2)
                elif (stuff1[row-1][column - 1] == 4 and stuff1[row][column] == 1 or stuff1[row-1][column - 1] == 1 and stuff1[row][column] == 4):
                    tmp.neighbor4Cost = (3*math.sqrt(2))/8
                elif (stuff1[row-1][column - 1] == 3 or stuff1[row][column] == 3):
                    tmp.neighbor4Cost = (3*math.sqrt(2))/2
                else:
                    tmp.neighbor4Cost = 0.7
            if (column - 1 >= 0 and stuff1[row][column] != 2 and stuff1[row][column - 1] != 2):
                tmp.neighbor5 = grid[row][column - 1]
                if (stuff1[row][column-1] == 1 and stuff1[row][column] == 1):
                    tmp.neighbor5Cost = 0.25
                elif (stuff1[row][column-1] == 3 and stuff1[row][column] == 3 or stuff1[row][column-1] == 4 and stuff1[row][column] == 3 or stuff1[row][column-1] == 3 and stuff1[row][column] == 4):
                    tmp.neighbor5Cost = 2
                elif (stuff1[row][column-1] == 4 and stuff1[row][column] == 4):
                    tmp.neighbor5Cost = 0.5
                elif (stuff1[row][column-1] == 4 and stuff1[row][column] == 1 or stuff1[row][column-1] == 1 and stuff1[row][column] == 4):
                    tmp.neighbor5Cost = 0.375
                elif (stuff1[row][column-1] == 3 or stuff1[row][column] == 3):
                    tmp.neighbor5Cost = 1.5
                else:
                    tmp.neighbor5Cost = 0.5

            if (row + 1 < 120 and column - 1 >= 0 and stuff1[row][column] != 2 and stuff1[row + 1][column - 1] != 2):
                tmp.neighbor6 = grid[row + 1][column - 1]
                if (stuff1[row+1][column - 1] == 1 and stuff1[row][column] == 1):
                    tmp.neighbor6Cost = 0.35
                elif (stuff1[row+1][column -1] == 3 and stuff1[row][column] == 3 or stuff1[row+1][column -1] == 4 and stuff1[row][column] == 3 or stuff1[row+1][column - 1] == 3 and stuff1[row][column] == 4):
                    tmp.neighbor6Cost = math.sqrt(8)
                elif (stuff1[row+1][column - 1] == 4 and stuff1[row][column] == 4):
                    tmp.neighbor6Cost = math.sqrt(2)
                elif (stuff1[row+1][column - 1] == 4 and stuff1[row][column] == 1 or stuff1[row+1][column - 1] == 1 and stuff1[row][column] == 4):
                    tmp.neighbor6Cost = (3*math.sqrt(2))/8
                elif (stuff1[row+1][column - 1] == 3 or stuff1[row][column] == 3):
                    tmp.neighbor6Cost = (3*math.sqrt(2))/2
                else:
                    tmp.neighbor6Cost = 0.7
            if (row + 1 < 120 and stuff1[row][column] != 2 and stuff1[row + 1][column] != 2):
                tmp.neighbor7 = grid[row + 1][column]
                if (stuff1[row+1][column] == 1 and stuff1[row][column] == 1):
                    tmp.neighbor7Cost = 0.25
                elif (stuff1[row+1][column] == 3 and stuff1[row][column] == 3 or stuff1[row+1][column] == 4 and stuff1[row][column] == 3 or stuff1[row+1][column] == 3 and stuff1[row][column] == 4):
                    tmp.neighbor7Cost = 2
                elif (stuff1[row+1][column] == 4 and stuff1[row][column] == 4):
                    tmp.neighbor7Cost = 0.5
                elif (stuff1[row+1][column] == 4 and stuff1[row][column] == 1 or stuff1[row+1][column] == 1 and stuff1[row][column] == 4):
                    tmp.neighbor7Cost = 0.375
                elif (stuff1[row+1][column] == 3 or stuff1[row][column] == 3):
                    tmp.neighbor7Cost = 1.5
                else:
                    tmp.neighbor7Cost = 0.5
            if (row + 1 < 120 and column + 1 < 160 and stuff1[row][column] != 2 and stuff1[row + 1][column + 1] != 2):
                tmp.neighbor8 = grid[row + 1][column + 1]
                if (stuff1[row+1][column + 1] == 1 and stuff1[row][column] == 1):
                    tmp.neighbor8Cost = 0.35
                elif (stuff1[row+1][column+1] == 3 and stuff1[row][column] == 3 or stuff1[row+1][column+1] == 4 and stuff1[row][column] == 3 or stuff1[row+1][column + 1] == 3 and stuff1[row][column] == 4):
                    tmp.neighbor8Cost = math.sqrt(8)
                elif (stuff1[row+1][column + 1] == 4 and stuff1[row][column] == 4):
                    tmp.neighbor8Cost = math.sqrt(2)
                elif (stuff1[row+1][column + 1] == 4 and stuff1[row][column] == 1 or stuff1[row+1][column + 1] == 1 and stuff1[row][column] == 4):
                    tmp.neighbor8Cost = (3*math.sqrt(2))/8
                elif (stuff1[row+1][column + 1] == 3 or stuff1[row][column] == 3):
                    tmp.neighbor8Cost = (3*math.sqrt(2))/2
                else:
                    tmp.neighbor8Cost = 0.7

def GenerateRandStart():
    x = randint(0, 119)
    y = randint(0, 159)
    start = grid[x][y]
    return start

def GenerateRandGoal():
    x = randint(0, 119)
    y = randint(0, 159)
    goal = grid[x][y]
    return goal
'''
def siftup(heap, item):

    child = len(heap)-1

    while (child > 0):
        parent = (child-1)/2
        if(int(parent)<0 or int(child)<0):
            break
        if(int(parent)>=len(heap) or int(child)>=len(heap)):
            break
        if (len(heap) == 0 or len(heap)==1):
            break
        if (heap[int(parent)].fx > heap[int(child)].fx):
            heap[int(child)] = heap[int(parent)]
            heap[int(parent)] = item
            child = parent
            parent = parent / 2
        else:
            break

def siftdown(heap, item):
    parent = 0#int(item.index)
    child = int(2 * parent + 1)

    while (child < int(len(heap))):

        max = child
        rightChild = child + 1

        if (rightChild < len(heap)):
            if (heap[rightChild].fx < heap[child].fx):
                max = max + 1

        if (heap[parent].fx > heap[max].fx):
            tmp = heap[parent]
            heap[parent] = heap[max]
            heap[max] = tmp
            parent = max
            child = 2 * parent + 1
        else:
            break

def pop(heap):
    if heap:
       # returnitem = heap.pop(0)  # heap[0]
        returnitem = heap.pop(0)

        if (len(heap) != 0):
            heap.insert(0, heap.pop(len(heap) - 1))
            siftdown(heap, heap[0])


    else:
        return None

    return returnitem

def push(heap, item):
    heap.append(item)
    #item.index = len(heap) - 1
    siftup(heap, item)#, item)

def UpdateVertex(fringe, node, neighborCost):
    gx = node.parent.gx + neighborCost
    fx = gx + hx(node, goal)
    if (fx > node.fx):
        node.fx = fx
        siftup(fringe, node)

    i = 0
    while(i < len(fringe)):

        if(fringe[i]==node):

            gx = node.parent.gx +neighborCost
            fx = gx + hx(node, goal)
            if(fx > node.fx):
                node.fx = fx
                siftup(fringe,node)
                break
        else:
            i=i+1

def UpdateVertexW(fringe, node, neighborCost, weight):
    gx = node.parent.gx + neighborCost
    fx = gx + hxW(node, goal, weight)
    if (fx < node.fx):
        node.fx = fx
        siftup(fringe, node)

def UpdateVertexUCS(fringe, node, neighborCost):
    gx = node.parent.gx + neighborCost
    fx = gx
    if (fx < node.fx):
        node.fx = fx
        siftup(fringe, node)

def hx(node, goal):
    result = math.sqrt(math.pow(goal.x - node.x, 2) + math.pow(goal.y - node.y, 2)) #euclidean
    #result=math.fabs(goal.x-node.x )+math.fabs(goal.y-node.y) #manhattan
    #result=max(math.fabs(goal.x-node.x),math.fabs(goal.y-node.y)) #chubbychub
    #result=(math.fabs(goal.x-node.x)/(node.x+goal.x+1))+(math.fabs(goal.y-node.y)/(node.y+goal.y+1))
    return result

def hxW(node, goal, weight):
    result = math.sqrt(math.pow(goal.x - node.x, 2) + math.pow(goal.y - node.y, 2))
    #result=math.fabs(goal.x-node.x )+math.fabs(goal.y-node.y)
    result = result * weight
    return result

def AStar(start, goal):
    nodesexpanded = 0

    start.fx = hx(start, goal)
    start.parent = None
    fringe = []
    closed = []
    push(fringe, start)
    fringeEmpty = 1
    while (fringeEmpty != 0):

        tmp = pop(fringe)
        fringeEmpty = fringeEmpty - 1
        if (tmp == goal):
            return tmp,nodesexpanded
        else:
            closed.append(tmp)
        if (tmp.neighbor1 != None):
            if (tmp.neighbor1 not in closed):
                if (tmp.neighbor1 not in fringe):
                    tmp.neighbor1.gx = tmp.gx + tmp.neighbor1Cost
                    tmp.neighbor1.hx = hx(tmp.neighbor1, goal)
                    tmp.neighbor1.fx = tmp.neighbor1.gx + tmp.neighbor1.hx
                    tmp.neighbor1.parent = tmp
                    push(fringe, tmp.neighbor1)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1

                else:
                    UpdateVertex(fringe, tmp.neighbor1, tmp.neighbor1Cost)
        if (tmp.neighbor2 != None):
            if (tmp.neighbor2 not in closed):
                if (tmp.neighbor2 not in fringe):
                    tmp.neighbor2.gx = tmp.gx + tmp.neighbor2Cost
                    tmp.neighbor2.hx = hx(tmp.neighbor2, goal)
                    tmp.neighbor2.fx = tmp.neighbor2.gx + tmp.neighbor2.hx
                    tmp.neighbor2.parent = tmp
                    push(fringe, tmp.neighbor2)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1

                else:
                    UpdateVertex(fringe, tmp.neighbor2, tmp.neighbor2Cost)

        if (tmp.neighbor3 != None):
            if (tmp.neighbor3 not in closed):
                if (tmp.neighbor3 not in fringe):
                    tmp.neighbor3.gx = tmp.gx + tmp.neighbor3Cost
                    tmp.neighbor3.hx = hx(tmp.neighbor3, goal)
                    tmp.neighbor3.fx = tmp.neighbor3.gx + tmp.neighbor3.hx
                    tmp.neighbor3.parent = tmp
                    push(fringe, tmp.neighbor3)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertex(fringe, tmp.neighbor3, tmp.neighbor3Cost)
        if (tmp.neighbor4 != None):
            if (tmp.neighbor4 not in closed):
                if (tmp.neighbor4 not in fringe):
                    tmp.neighbor4.gx = tmp.gx + tmp.neighbor4Cost
                    tmp.neighbor4.hx = hx(tmp.neighbor4, goal)
                    tmp.neighbor4.fx = tmp.neighbor4.gx + tmp.neighbor4.hx
                    tmp.neighbor4.parent = tmp
                    push(fringe, tmp.neighbor4)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertex(fringe, tmp.neighbor4, tmp.neighbor4Cost)
        if (tmp.neighbor5 != None):
            if (tmp.neighbor5 not in closed):
                if (tmp.neighbor5 not in fringe):
                    tmp.neighbor5.gx = tmp.gx + tmp.neighbor5Cost
                    tmp.neighbor5.hx = hx(tmp.neighbor5, goal)
                    tmp.neighbor5.fx = tmp.neighbor5.gx + tmp.neighbor5.hx
                    tmp.neighbor5.parent = tmp
                    push(fringe, tmp.neighbor5)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertex(fringe, tmp.neighbor5, tmp.neighbor5Cost)
        if (tmp.neighbor6 != None):
            if (tmp.neighbor6 not in closed):
                if (tmp.neighbor6 not in fringe):
                    tmp.neighbor6.gx = tmp.gx + tmp.neighbor6Cost
                    tmp.neighbor6.hx = hx(tmp.neighbor6, goal)
                    tmp.neighbor6.fx = tmp.neighbor6.gx + tmp.neighbor6.hx
                    tmp.neighbor6.parent = tmp
                    push(fringe, tmp.neighbor6)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertex(fringe, tmp.neighbor6, tmp.neighbor6Cost)
        if (tmp.neighbor7 != None):
            if (tmp.neighbor7 not in closed):
                if (tmp.neighbor7 not in fringe):
                    tmp.neighbor7.gx = tmp.gx + tmp.neighbor7Cost
                    tmp.neighbor7.hx = hx(tmp.neighbor7, goal)
                    tmp.neighbor7.fx = tmp.neighbor7.gx + tmp.neighbor7.hx
                    tmp.neighbor7.parent = tmp
                    push(fringe, tmp.neighbor7)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertex(fringe, tmp.neighbor7, tmp.neighbor7Cost)
        if (tmp.neighbor8 != None):
            if (tmp.neighbor8 not in closed):
                if (tmp.neighbor8 not in fringe):
                    tmp.neighbor8.gx = tmp.gx + tmp.neighbor8Cost
                    tmp.neighbor8.hx = hx(tmp.neighbor8, goal)
                    tmp.neighbor8.fx = tmp.neighbor8.gx + tmp.neighbor8.hx
                    tmp.neighbor8.parent = tmp
                    push(fringe, tmp.neighbor8)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertex(fringe, tmp.neighbor8, tmp.neighbor8Cost)

def WeightedAStar(start, goal, weight):
    nodesexpanded=0
    start.fx = hxW(start, goal, weight)
    start.parent = None
    fringe = []
    closed = []
    push(fringe, start)
    fringeEmpty = 1

    while (fringeEmpty != 0):
        tmp = pop(fringe)
        fringeEmpty = fringeEmpty - 1
        if (tmp == goal):
            return tmp,nodesexpanded
        else:
            closed.append(tmp)

        if (tmp.neighbor1 != None):
            if (tmp.neighbor1 not in closed):
                if (tmp.neighbor1 not in fringe):
                    tmp.neighbor1.gx = tmp.gx + tmp.neighbor1Cost
                    tmp.neighbor1.hx = hxW(tmp.neighbor1, goal, weight)
                    tmp.neighbor1.fx = tmp.neighbor1.gx + tmp.neighbor1.hx
                    tmp.neighbor1.parent = tmp
                    push(fringe, tmp.neighbor1)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexW(fringe, tmp.neighbor1, tmp.neighbor1Cost, weight)
        if (tmp.neighbor2 != None):
            if (tmp.neighbor2 not in closed):
                if (tmp.neighbor2 not in fringe):
                    tmp.neighbor2.gx = tmp.gx + tmp.neighbor2Cost
                    tmp.neighbor2.hx = hxW(tmp.neighbor2, goal, weight)
                    tmp.neighbor2.fx = tmp.neighbor2.gx + tmp.neighbor2.hx
                    tmp.neighbor2.parent = tmp
                    push(fringe, tmp.neighbor2)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexW(fringe, tmp.neighbor2, tmp.neighbor2Cost, weight)

        if (tmp.neighbor3 != None):
            if (tmp.neighbor3 not in closed):
                if (tmp.neighbor3 not in fringe):
                    tmp.neighbor3.gx = tmp.gx + tmp.neighbor3Cost
                    tmp.neighbor3.hx = hxW(tmp.neighbor3, goal, weight)
                    tmp.neighbor3.fx = tmp.neighbor3.gx + tmp.neighbor3.hx
                    tmp.neighbor3.parent = tmp
                    push(fringe, tmp.neighbor3)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexW(fringe, tmp.neighbor3, tmp.neighbor3Cost, weight)
        if (tmp.neighbor4 != None):
            if (tmp.neighbor4 not in closed):
                if (tmp.neighbor4 not in fringe):
                    tmp.neighbor4.gx = tmp.gx + tmp.neighbor4Cost
                    tmp.neighbor4.hx = hxW(tmp.neighbor4, goal, weight)
                    tmp.neighbor4.fx = tmp.neighbor4.gx + tmp.neighbor4.hx
                    tmp.neighbor4.parent = tmp
                    push(fringe, tmp.neighbor4)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexW(fringe, tmp.neighbor4, tmp.neighbor4Cost, weight)
        if (tmp.neighbor5 != None):
            if (tmp.neighbor5 not in closed):
                if (tmp.neighbor5 not in fringe):
                    tmp.neighbor5.gx = tmp.gx + tmp.neighbor5Cost
                    tmp.neighbor5.hx = hxW(tmp.neighbor5, goal, weight)
                    tmp.neighbor5.fx = tmp.neighbor5.gx + tmp.neighbor5.hx
                    tmp.neighbor5.parent = tmp
                    push(fringe, tmp.neighbor5)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexW(fringe, tmp.neighbor5, tmp.neighbor5Cost, weight)
        if (tmp.neighbor6 != None):
            if (tmp.neighbor6 not in closed):
                if (tmp.neighbor6 not in fringe):
                    tmp.neighbor6.gx = tmp.gx + tmp.neighbor6Cost
                    tmp.neighbor6.hx = hxW(tmp.neighbor6, goal, weight)
                    tmp.neighbor6.fx = tmp.neighbor6.gx + tmp.neighbor6.hx
                    tmp.neighbor6.parent = tmp
                    push(fringe, tmp.neighbor6)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexW(fringe, tmp.neighbor6, tmp.neighbor6Cost, weight)
        if (tmp.neighbor7 != None):
            if (tmp.neighbor7 not in closed):
                if (tmp.neighbor7 not in fringe):
                    tmp.neighbor7.gx = tmp.gx + tmp.neighbor7Cost
                    tmp.neighbor7.hx = hxW(tmp.neighbor7, goal, weight)
                    tmp.neighbor7.fx = tmp.neighbor7.gx + tmp.neighbor7.hx
                    tmp.neighbor7.parent = tmp
                    push(fringe, tmp.neighbor7)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexW(fringe, tmp.neighbor7, tmp.neighbor7Cost, weight)
        if (tmp.neighbor8 != None):
            if (tmp.neighbor8 not in closed):
                if (tmp.neighbor8 not in fringe):
                    tmp.neighbor8.gx = tmp.gx + tmp.neighbor8Cost
                    tmp.neighbor8.hx = hxW(tmp.neighbor8, goal, weight)
                    tmp.neighbor8.fx = tmp.neighbor8.gx + tmp.neighbor8.hx
                    tmp.neighbor8.parent = tmp
                    push(fringe, tmp.neighbor8)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexW(fringe, tmp.neighbor8, tmp.neighbor8Cost, weight)

def USC(start, goal):
    nodesexpanded=0
    start.fx = 0
    start.parent = None
    fringe = []
    closed = []
    push(fringe, start)
    fringeEmpty = 1
    while (fringeEmpty != 0):
        tmp = pop(fringe)
        fringeEmpty = fringeEmpty - 1
        if (tmp == goal):
            return tmp,nodesexpanded
        else:
            closed.append(tmp)
        if (tmp.neighbor1 != None):
            if (tmp.neighbor1 not in closed):
                if (tmp.neighbor1 not in fringe):
                    tmp.neighbor1.gx = tmp.gx + tmp.neighbor1Cost
                    tmp.neighbor1.fx = tmp.neighbor1.gx
                    tmp.neighbor1.parent = tmp
                    push(fringe, tmp.neighbor1)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexUCS(fringe, tmp.neighbor1, tmp.neighbor1Cost)
        if (tmp.neighbor2 != None):
            if (tmp.neighbor2 not in closed):
                if (tmp.neighbor2 not in fringe):
                    tmp.neighbor2.gx = tmp.gx + tmp.neighbor2Cost
                    tmp.neighbor2.fx = tmp.neighbor2.gx
                    tmp.neighbor2.parent = tmp
                    push(fringe, tmp.neighbor2)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexUCS(fringe, tmp.neighbor2, tmp.neighbor2Cost)

        if (tmp.neighbor3 != None):
            if (tmp.neighbor3 not in closed):
                if (tmp.neighbor3 not in fringe):
                    tmp.neighbor3.gx = tmp.gx + tmp.neighbor3Cost
                    tmp.neighbor3.fx = tmp.neighbor3.gx
                    tmp.neighbor3.parent = tmp
                    push(fringe, tmp.neighbor3)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexUCS(fringe, tmp.neighbor3, tmp.neighbor3Cost)
        if (tmp.neighbor4 != None):
            if (tmp.neighbor4 not in closed):
                if (tmp.neighbor4 not in fringe):
                    tmp.neighbor4.gx = tmp.gx + tmp.neighbor4Cost
                    tmp.neighbor4.fx = tmp.neighbor4.gx
                    tmp.neighbor4.parent = tmp
                    push(fringe, tmp.neighbor4)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexUCS(fringe, tmp.neighbor4, tmp.neighbor4Cost)
        if (tmp.neighbor5 != None):
            if (tmp.neighbor5 not in closed):
                if (tmp.neighbor5 not in fringe):
                    tmp.neighbor5.gx = tmp.gx + tmp.neighbor5Cost
                    tmp.neighbor5.fx = tmp.neighbor5.gx
                    tmp.neighbor5.parent = tmp
                    push(fringe, tmp.neighbor5)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexUCS(fringe, tmp.neighbor5, tmp.neighbor5Cost)
        if (tmp.neighbor6 != None):
            if (tmp.neighbor6 not in closed):
                if (tmp.neighbor6 not in fringe):
                    tmp.neighbor6.gx = tmp.gx + tmp.neighbor6Cost
                    tmp.neighbor6.fx = tmp.neighbor6.gx
                    tmp.neighbor6.parent = tmp
                    push(fringe, tmp.neighbor6)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexUCS(fringe, tmp.neighbor6, tmp.neighbor6Cost)
        if (tmp.neighbor7 != None):
            if (tmp.neighbor7 not in closed):
                if (tmp.neighbor7 not in fringe):
                    tmp.neighbor7.gx = tmp.gx + tmp.neighbor7Cost
                    tmp.neighbor7.fx = tmp.neighbor7.gx
                    tmp.neighbor7.parent = tmp
                    push(fringe, tmp.neighbor7)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexUCS(fringe, tmp.neighbor7, tmp.neighbor7Cost)
        if (tmp.neighbor8 != None):
            if (tmp.neighbor8 not in closed):
                if (tmp.neighbor8 not in fringe):
                    tmp.neighbor8.gx = tmp.gx + tmp.neighbor8Cost
                    tmp.neighbor8.fx = tmp.neighbor8.gx
                    tmp.neighbor8.parent = tmp
                    push(fringe, tmp.neighbor8)
                    fringeEmpty = fringeEmpty + 1
                    nodesexpanded +=1
                else:
                    UpdateVertexUCS(fringe, tmp.neighbor8, tmp.neighbor8Cost)
'''





def makePartialBlock(tmpGrid):
    center=[]
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
        center.append((tmpRow,tmpCol))
        for a in range(tmpRow - 15, tmpRow + 16):
            if (a >= 120):
                break
            elif (a < 0):
                break
            for b in range(tmpCol - 15, tmpCol + 16):
                if (b >= 160):
                    break
                elif (b < 0):
                    break
                try:
                    willBlock = randint(0, 1)
                    if (willBlock == 1):
                        tmpGrid[a][b].hardToTraverse = True
                        tmpGrid[a][b].color = (100, 100, 100)
                except NameError:
                    pass

    return tmpGrid,center

def makeRiverIter(tmpMap):
    BMap=copy.deepcopy(tmpMap)
    CMap=copy.deepcopy(tmpMap)
    totCount=0
    counter=0
    while(counter<4):
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
                print ("redo")
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
        if (totCount>20):
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
            if (map[row][col]==0):
                map[row][col] = 1
                dist = dist + 1
                col = col + 1
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
            if (map[row][col] ==0):
                map[row][col] = 1
                dist = dist + 1
                col = col - 1
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
            if (map[row][col] == 0):
                map[row][col] = 1
                dist = dist + 1
                row = row - 1

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
            if (map[row][col] == 0):
                map[row][col] = 1
                dist = dist + 1
                row = row + 1

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

def outputFile(tmpGrid,centerstuff,startRow,startCol,endRow,endCol):
    fileobj=open("test5.txt", 'w')
    a=str(startRow)
    b=str(startCol)
    start='('+ a+','+ b+')'
    fileobj.write(start+"\n")
    c=str(endRow)
    d=str(endCol)
    goal='('+ c+','+ d+')'
    fileobj.write(goal+"\n")
    for i in range(8):
        if(i==7):
            fileobj.write(str(centerstuff[i]))
        else:
            fileobj.write(str(centerstuff[i])+'\n')

    for row in range(120):
        str1=''
        for col in range(160):
            if(tmpGrid[row][col].block==True):
                str1=str1+'0'
            elif(tmpGrid[row][col].hasRiver):
                if(tmpGrid[row][col].hardToTraverse):
                    str1=str1+'b'
                else:
                    str1=str1+'a'
            elif(tmpGrid[row][col].hardToTraverse):
                str1=str1+'2'
            else:
                str1=str1+'1'
        fileobj.write("\n"+str1)
    fileobj.close()

def insertFile(file):
    grid=[]
    stuff=[]
    file_obj=open(file,'r')
    start=file_obj.readline()
    start1=Node()
    goal=Node()
    firstrownum=start.index(',')
    firstrow=start[1:firstrownum]
    firstcol=start[firstrownum+1:len(start)-2]
    secondLine=file_obj.readline()
    secondrownum=secondLine.index(',')
    secondrow=secondLine[1:secondrownum]
    secondcol=secondLine[secondrownum+1:len(secondLine)-2]
    for i in range(8):
        randlines=file_obj.readline()

    for i in range(120):#0 reg, 1 is riv, 2 is blocked
        grid.append([])
        stuff.append([])
        tmp=file_obj.readline()
        for num in range(160):
            tmpNode = Node()
            grid[i].append(tmpNode)
            stuff[i].append(0)
            grid[i][num].center = ((MARGIN + WIDTH) * num + MARGIN + 3, (MARGIN + HEIGHT) * i + MARGIN + 2.5)
            if(tmp[num]==0 or tmp[num]=='0'):
                grid[i][num].color=(0,0,0)
                grid[i][num].block=True
                stuff[i][num]=2
            elif(tmp[num]==1 or tmp[num]=='1'):
                grid[i][num].color=(255,255,255)
                stuff[i][num]=0
            elif(tmp[num]==2 or tmp[num]=='2'):
                grid[i][num].color=(100,100,100)
                grid[i][num].hardToTraverse=True
                stuff[i][num]=3
            elif(tmp[num]=='a'):
                grid[i][num].color=(0,0,255)
                grid[i][num].hasRiver=True
                stuff[i][num]=1
            elif(tmp[num]=='b'):
                grid[i][num].color=(0,0,255)
                grid[i][num].hasRiver=True
                grid[i][num].hardToTraverse=True
                stuff[i][num]=4
            if(i==int(float(firstrow)) and num==int(float(firstcol))):
                grid[i][num].start=True
                grid[i][num].color=(0,255,0)
                start1=grid[i][num]
            elif(i==int(float(secondrow)) and num==int(float(secondcol))):
                grid[i][num].finish=True
                grid[i][num].color=(255,0,0)
                goal=grid[i][num]

    file_obj.close()
    return grid,stuff,start1,goal

def texts(wantedtext,a,b,c):
    font = pygame.font.Font(None, 20)
    scoretext = font.render(wantedtext, 1, (0, 255, 0))
    screen.blit(scoretext, (1120, 10))
    tmp1 = font.render(a, 1, (0, 255, 0))
    screen.blit(tmp1, (1120, 30))
    tmp2 = font.render(b, 1, (0, 255, 0))
    screen.blit(tmp2, (1120, 50))
    tmp3 = font.render(c, 1, (0, 255, 0))
    screen.blit(tmp3, (1120, 70))


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
grid,center=makePartialBlock(grid)
# Initialize pygame
t0=1


# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 6
HEIGHT = 5
# This sets the margin between each cell
MARGIN = 1
rivcount=0
ans=input("would you like to insert a file?")
if(ans=='yes'):
    fileName=input("what is the name of the file")
    grid,stuff1,start,goal=insertFile(fileName)
    t0=time.clock()
    connectTheDots()
else:

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
            if stuff1[row][column] == 1:#has river
                grid[row][column].color=(0,0,255)
                grid[row][column].hasRiver=True
            elif(stuff1[row][column]==2):#blocked
                grid[row][column].color=(0,0,0)
                grid[row][column].block=True
            elif(stuff1[row][column]==5):#start
                grid[row][column].color=(0,255,0)
                grid[row][column].start=True
            elif(stuff1[row][column]==6):#finish
                grid[row][column].color=(255,0,0)
                grid[row][column].finish=True

    for row in range(120):
        str1=''
        for col in range(160):
            if(grid[row][col].block==True):
                stuff1[row][col]=2
            elif(grid[row][col].hasRiver):
                if(grid[row][col].hardToTraverse):
                    stuff1[row][col]=4
                else:
                    stuff1[row][col]=1
            elif(grid[row][col].hardToTraverse):
                stuff1[row][col] = 3
            else:
                stuff1[row][col] = 0

    for row in range(120):
        for column in range(160):
            color = grid[row][column].color
            if stuff1[row][column] == 1:
                grid[row][column].color=(0,0,255)
            elif(stuff1[row][column]==2):
                grid[row][column].color=(0,0,0)
            grid[row][column].center = ((MARGIN + WIDTH)* column + MARGIN + 3, (MARGIN + HEIGHT)*row + MARGIN + 2.5)


    # -------- Main Program Loop -----------
    connectTheDots()

    start = GenerateRandStart()
    while (stuff1[start.x][start.y] == 2):
        start = GenerateRandStart()

    goal = GenerateRandGoal()
    while (stuff1[goal.x][goal.y] == 2):
        goal = GenerateRandGoal()

    while(math.sqrt(math.pow(goal.x-start.x,2)+math.pow(goal.y-start.y,2))<100):
        start = GenerateRandStart()
        while (stuff1[start.x][start.y] == 2):
            start = GenerateRandStart()

        goal = GenerateRandGoal()
        while (stuff1[goal.x][goal.y] == 2):
            goal = GenerateRandGoal()


    start.color=(0,255,0)
    goal.color=(255,0,0)
    toSave=input("would you like to save this map?")
    if(toSave=="yes"):
        outputFile(grid,center,start.x,start.y,goal.x,goal.y)


randcount = 0
whichSearch=input("which search would you like to use? 1 for AStar, 2 for weighted AStar, and 3 for UCS")
if(whichSearch=='1'):
    search1=AStarSearchAlgorithm(start,goal)
    tmp,nodesexpanded=search1.Search()
    print("Fx")
    print(tmp.fx)
    print("Gx")
    print(tmp.gx)
    print("Hx")
    print(tmp.hx)
elif (whichSearch=='2'):
    weight=input("what would you like the weight to be?")
    search3=WeightedAStarSearch(start,goal,int(float(weight)))
    #tmp,nodesexpanded=WeightedAStar(start,goal,int(float(weight)))
    tmp,nodesexpanded=search3.Search()
    print("Fx")
    print(tmp.fx)
    print("Gx")
    print(tmp.gx)
    print("Hx")
    print(tmp.hx)
else:
    search2=UniformCostSearch(start,goal)
    tmp,nodesexpanded=search2.Search()
    #tmp,nodesexpanded=USC(start,goal)
    print("Fx")
    print(tmp.fx)
    print("Gx")
    print(tmp.gx)
    print("Hx")
    print(tmp.hx)
t2=time.clock()

riv=[]
from pympler import asizeof
sizecount=0
while (tmp != None and randcount == 0):
    #print("[", tmp.x, "]", "[", tmp.y, "]")
    riv.append((grid[tmp.x][tmp.y].center))
    #sizecount+=asizeof.asizeof(tmp)
    tmp = tmp.parent

print (sizecount/1000000)
print(nodesexpanded)
print(t2-t0)

randcount = randcount+1



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
toinput=''
hinput=''
ginput=''
finput=''
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
                #grid[row][column].color = (0, 150, 255)
                hxtmp=grid[row][column].hx
                gxtmp=grid[row][column].gx
                fxtmp=grid[row][column].fx
                toinput='x: '+str(column)+" y: "+str(row)
                hinput='h: ' + str(hxtmp)
                ginput='g: '+str(gxtmp)
                finput='f: '+str(fxtmp)
                texts(toinput,hinput,ginput,finput)
                #print("Click ", pos, "Grid coordinates: ", row, column)
            except IndexError:
                print("Hey dont click there")

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(120):
        for column in range(160):
            color = grid[row][column].color
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    # list = [grid[50][0].centerLeft, grid[50][100].centerLeft]
    pygame.draw.lines(screen, (0, 255, 0), False, riv, 2)

    texts(toinput, hinput, ginput, finput)

    pygame.display.flip()


# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()