import math


class AStarSearchAlgorithm():

    def __init__(self,start,goal):
        self.start=start
        self.goal=goal

    def Search(self):
        nodesexpanded = 0

        self.start.fx = self.hx(self.start, self.goal)
        self.start.parent = None
        fringe = []
        closed = []
        self.push(fringe, self.start)
        fringeEmpty = 1
        while (fringeEmpty != 0):

            tmp = self.pop(fringe)
            fringeEmpty = fringeEmpty - 1
            if (tmp == self.goal):
                return tmp, nodesexpanded
            else:
                closed.append(tmp)
            if (tmp.neighbor1 != None):
                if (tmp.neighbor1 not in closed):
                    if (tmp.neighbor1 not in fringe):
                        tmp.neighbor1.gx = tmp.gx + tmp.neighbor1Cost
                        tmp.neighbor1.hx = self.hx(tmp.neighbor1, self.goal)
                        tmp.neighbor1.fx = tmp.neighbor1.gx + tmp.neighbor1.hx
                        tmp.neighbor1.parent = tmp
                        self.push(fringe, tmp.neighbor1)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1

                    else:
                        self.UpdateVertex(fringe, tmp.neighbor1, tmp.neighbor1Cost)
            if (tmp.neighbor2 != None):
                if (tmp.neighbor2 not in closed):
                    if (tmp.neighbor2 not in fringe):
                        tmp.neighbor2.gx = tmp.gx + tmp.neighbor2Cost
                        tmp.neighbor2.hx = self.hx(tmp.neighbor2, self.goal)
                        tmp.neighbor2.fx = tmp.neighbor2.gx + tmp.neighbor2.hx
                        tmp.neighbor2.parent = tmp
                        self.push(fringe, tmp.neighbor2)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1

                    else:
                        self.UpdateVertex(fringe, tmp.neighbor2, tmp.neighbor2Cost)

            if (tmp.neighbor3 != None):
                if (tmp.neighbor3 not in closed):
                    if (tmp.neighbor3 not in fringe):
                        tmp.neighbor3.gx = tmp.gx + tmp.neighbor3Cost
                        tmp.neighbor3.hx = self.hx(tmp.neighbor3, self.goal)
                        tmp.neighbor3.fx = tmp.neighbor3.gx + tmp.neighbor3.hx
                        tmp.neighbor3.parent = tmp
                        self.push(fringe, tmp.neighbor3)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertex(fringe, tmp.neighbor3, tmp.neighbor3Cost)
            if (tmp.neighbor4 != None):
                if (tmp.neighbor4 not in closed):
                    if (tmp.neighbor4 not in fringe):
                        tmp.neighbor4.gx = tmp.gx + tmp.neighbor4Cost
                        tmp.neighbor4.hx = self.hx(tmp.neighbor4, self.goal)
                        tmp.neighbor4.fx = tmp.neighbor4.gx + tmp.neighbor4.hx
                        tmp.neighbor4.parent = tmp
                        self.push(fringe, tmp.neighbor4)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertex(fringe, tmp.neighbor4, tmp.neighbor4Cost)
            if (tmp.neighbor5 != None):
                if (tmp.neighbor5 not in closed):
                    if (tmp.neighbor5 not in fringe):
                        tmp.neighbor5.gx = tmp.gx + tmp.neighbor5Cost
                        tmp.neighbor5.hx = self.hx(tmp.neighbor5, self.goal)
                        tmp.neighbor5.fx = tmp.neighbor5.gx + tmp.neighbor5.hx
                        tmp.neighbor5.parent = tmp
                        self.push(fringe, tmp.neighbor5)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertex(fringe, tmp.neighbor5, tmp.neighbor5Cost)
            if (tmp.neighbor6 != None):
                if (tmp.neighbor6 not in closed):
                    if (tmp.neighbor6 not in fringe):
                        tmp.neighbor6.gx = tmp.gx + tmp.neighbor6Cost
                        tmp.neighbor6.hx = self.hx(tmp.neighbor6, self.goal)
                        tmp.neighbor6.fx = tmp.neighbor6.gx + tmp.neighbor6.hx
                        tmp.neighbor6.parent = tmp
                        self.push(fringe, tmp.neighbor6)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertex(fringe, tmp.neighbor6, tmp.neighbor6Cost)
            if (tmp.neighbor7 != None):
                if (tmp.neighbor7 not in closed):
                    if (tmp.neighbor7 not in fringe):
                        tmp.neighbor7.gx = tmp.gx + tmp.neighbor7Cost
                        tmp.neighbor7.hx = self.hx(tmp.neighbor7, self.goal)
                        tmp.neighbor7.fx = tmp.neighbor7.gx + tmp.neighbor7.hx
                        tmp.neighbor7.parent = tmp
                        self.push(fringe, tmp.neighbor7)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertex(fringe, tmp.neighbor7, tmp.neighbor7Cost)
            if (tmp.neighbor8 != None):
                if (tmp.neighbor8 not in closed):
                    if (tmp.neighbor8 not in fringe):
                        tmp.neighbor8.gx = tmp.gx + tmp.neighbor8Cost
                        tmp.neighbor8.hx = self.hx(tmp.neighbor8, self.goal)
                        tmp.neighbor8.fx = tmp.neighbor8.gx + tmp.neighbor8.hx
                        tmp.neighbor8.parent = tmp
                        self.push(fringe, tmp.neighbor8)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertex(fringe, tmp.neighbor8, tmp.neighbor8Cost)

    def hx(self,node, goal):
        result = math.sqrt(math.pow(goal.x - node.x, 2) + math.pow(goal.y - node.y, 2))  # euclidean
        # result=math.fabs(goal.x-node.x )+math.fabs(goal.y-node.y) #manhattan
        # result=max(math.fabs(goal.x-node.x),math.fabs(goal.y-node.y)) #chubbychub
        # result=(math.fabs(goal.x-node.x)/(node.x+goal.x+1))+(math.fabs(goal.y-node.y)/(node.y+goal.y+1))
        return result

    def siftup(self,heap, item):

            child = len(heap) - 1

            while (child > 0):
                parent = (child - 1) / 2
                if (int(parent) < 0 or int(child) < 0):
                    break
                if (int(parent) >= len(heap) or int(child) >= len(heap)):
                    break
                if (len(heap) == 0 or len(heap) == 1):
                    break
                if (heap[int(parent)].fx > heap[int(child)].fx):
                    heap[int(child)] = heap[int(parent)]
                    heap[int(parent)] = item
                    child = parent
                    parent = parent / 2
                else:
                    break

    def push(self,heap, item):
        heap.append(item)
        # item.index = len(heap) - 1
        self.siftup(heap, item)  # , item)

    def siftdown(self,heap, item):
        parent = 0  # int(item.index)
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

    def pop(self,heap):
        if heap:
            # returnitem = heap.pop(0)  # heap[0]
            returnitem = heap.pop(0)

            if (len(heap) != 0):
                heap.insert(0, heap.pop(len(heap) - 1))
                self.siftdown(heap, heap[0])


        else:
            return None

        return returnitem

    def UpdateVertex(self,fringe, node, neighborCost):
        gx = node.parent.gx + neighborCost
        fx = gx + self.hx(node, self.goal)
        if (fx > node.fx):
            node.fx = fx
            self.siftup(fringe, node)

        """i = 0
        while(i < len(fringe)):

            if(fringe[i]==node):

                gx = node.parent.gx +neighborCost
                fx = gx + hx(node, goal)
                if(fx > node.fx):
                    node.fx = fx
                    siftup(fringe,node)
                    break
            else:
                i=i+1"""


class UniformCostSearch(AStarSearchAlgorithm):
    def heristic(self):
        print( "uniform heristic")
    def Search(self):
        nodesexpanded = 0
        self.start.fx = 0
        self.start.parent = None
        fringe = []
        closed = []
        self.push(fringe, self.start)
        fringeEmpty = 1
        while (fringeEmpty != 0):
            tmp = self.pop(fringe)
            fringeEmpty = fringeEmpty - 1
            if (tmp == self.goal):
                return tmp, nodesexpanded
            else:
                closed.append(tmp)
            if (tmp.neighbor1 != None):
                if (tmp.neighbor1 not in closed):
                    if (tmp.neighbor1 not in fringe):
                        tmp.neighbor1.gx = tmp.gx + tmp.neighbor1Cost
                        tmp.neighbor1.fx = tmp.neighbor1.gx
                        tmp.neighbor1.parent = tmp
                        self.push(fringe, tmp.neighbor1)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexUCS(fringe, tmp.neighbor1, tmp.neighbor1Cost)
            if (tmp.neighbor2 != None):
                if (tmp.neighbor2 not in closed):
                    if (tmp.neighbor2 not in fringe):
                        tmp.neighbor2.gx = tmp.gx + tmp.neighbor2Cost
                        tmp.neighbor2.fx = tmp.neighbor2.gx
                        tmp.neighbor2.parent = tmp
                        self.push(fringe, tmp.neighbor2)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexUCS(fringe, tmp.neighbor2, tmp.neighbor2Cost)

            if (tmp.neighbor3 != None):
                if (tmp.neighbor3 not in closed):
                    if (tmp.neighbor3 not in fringe):
                        tmp.neighbor3.gx = tmp.gx + tmp.neighbor3Cost
                        tmp.neighbor3.fx = tmp.neighbor3.gx
                        tmp.neighbor3.parent = tmp
                        self.push(fringe, tmp.neighbor3)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexUCS(fringe, tmp.neighbor3, tmp.neighbor3Cost)
            if (tmp.neighbor4 != None):
                if (tmp.neighbor4 not in closed):
                    if (tmp.neighbor4 not in fringe):
                        tmp.neighbor4.gx = tmp.gx + tmp.neighbor4Cost
                        tmp.neighbor4.fx = tmp.neighbor4.gx
                        tmp.neighbor4.parent = tmp
                        self.push(fringe, tmp.neighbor4)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexUCS(fringe, tmp.neighbor4, tmp.neighbor4Cost)
            if (tmp.neighbor5 != None):
                if (tmp.neighbor5 not in closed):
                    if (tmp.neighbor5 not in fringe):
                        tmp.neighbor5.gx = tmp.gx + tmp.neighbor5Cost
                        tmp.neighbor5.fx = tmp.neighbor5.gx
                        tmp.neighbor5.parent = tmp
                        self.push(fringe, tmp.neighbor5)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexUCS(fringe, tmp.neighbor5, tmp.neighbor5Cost)
            if (tmp.neighbor6 != None):
                if (tmp.neighbor6 not in closed):
                    if (tmp.neighbor6 not in fringe):
                        tmp.neighbor6.gx = tmp.gx + tmp.neighbor6Cost
                        tmp.neighbor6.fx = tmp.neighbor6.gx
                        tmp.neighbor6.parent = tmp
                        self.push(fringe, tmp.neighbor6)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexUCS(fringe, tmp.neighbor6, tmp.neighbor6Cost)
            if (tmp.neighbor7 != None):
                if (tmp.neighbor7 not in closed):
                    if (tmp.neighbor7 not in fringe):
                        tmp.neighbor7.gx = tmp.gx + tmp.neighbor7Cost
                        tmp.neighbor7.fx = tmp.neighbor7.gx
                        tmp.neighbor7.parent = tmp
                        self.push(fringe, tmp.neighbor7)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexUCS(fringe, tmp.neighbor7, tmp.neighbor7Cost)
            if (tmp.neighbor8 != None):
                if (tmp.neighbor8 not in closed):
                    if (tmp.neighbor8 not in fringe):
                        tmp.neighbor8.gx = tmp.gx + tmp.neighbor8Cost
                        tmp.neighbor8.fx = tmp.neighbor8.gx
                        tmp.neighbor8.parent = tmp
                        self.push(fringe, tmp.neighbor8)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexUCS(fringe, tmp.neighbor8, tmp.neighbor8Cost)

    def UpdateVertexUCS(self,fringe, node, neighborCost):
        gx = node.parent.gx + neighborCost
        fx = gx
        if (fx < node.fx):
            node.fx = fx
            self.siftup(fringe, node)

class WeightedAStarSearch(AStarSearchAlgorithm):
    def __init__(self,start,goal,weight):
        super().__init__(start,goal)
        self.weight = weight

    def hx(self,node,goal,weight):
        result = math.sqrt(math.pow(goal.x - node.x, 2) + math.pow(goal.y - node.y, 2))
        # result=math.fabs(goal.x-node.x )+math.fabs(goal.y-node.y)
        result = result * weight
        return result

    def UpdateVertexW(self,fringe, node, neighborCost, weight):
        gx = node.parent.gx + neighborCost
        fx = gx + self.hx(node, self.goal, weight)
        if (fx < node.fx):
            node.fx = fx
            self.siftup(fringe, node)

    def Search(self):
        nodesexpanded = 0
        self.start.fx = self.hx(self.start, self.goal, self.weight)
        self.start.parent = None
        fringe = []
        closed = []
        self.push(fringe, self.start)
        fringeEmpty = 1

        while (fringeEmpty != 0):
            tmp = self.pop(fringe)
            fringeEmpty = fringeEmpty - 1
            if (tmp == self.goal):
                return tmp, nodesexpanded
            else:
                closed.append(tmp)

            if (tmp.neighbor1 != None):
                if (tmp.neighbor1 not in closed):
                    if (tmp.neighbor1 not in fringe):
                        tmp.neighbor1.gx = tmp.gx + tmp.neighbor1Cost
                        tmp.neighbor1.hx = self.hx(tmp.neighbor1, self.goal, self.weight)
                        tmp.neighbor1.fx = tmp.neighbor1.gx + tmp.neighbor1.hx
                        tmp.neighbor1.parent = tmp
                        self.push(fringe, tmp.neighbor1)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexW(fringe, tmp.neighbor1, tmp.neighbor1Cost, self.weight)
            if (tmp.neighbor2 != None):
                if (tmp.neighbor2 not in closed):
                    if (tmp.neighbor2 not in fringe):
                        tmp.neighbor2.gx = tmp.gx + tmp.neighbor2Cost
                        tmp.neighbor2.hx = self.hx(tmp.neighbor2, self.goal, self.weight)
                        tmp.neighbor2.fx = tmp.neighbor2.gx + tmp.neighbor2.hx
                        tmp.neighbor2.parent = tmp
                        self.push(fringe, tmp.neighbor2)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexW(fringe, tmp.neighbor2, tmp.neighbor2Cost, self.weight)

            if (tmp.neighbor3 != None):
                if (tmp.neighbor3 not in closed):
                    if (tmp.neighbor3 not in fringe):
                        tmp.neighbor3.gx = tmp.gx + tmp.neighbor3Cost
                        tmp.neighbor3.hx = self.hx(tmp.neighbor3, self.goal, self.weight)
                        tmp.neighbor3.fx = tmp.neighbor3.gx + tmp.neighbor3.hx
                        tmp.neighbor3.parent = tmp
                        self.push(fringe, tmp.neighbor3)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexW(fringe, tmp.neighbor3, tmp.neighbor3Cost, self.weight)
            if (tmp.neighbor4 != None):
                if (tmp.neighbor4 not in closed):
                    if (tmp.neighbor4 not in fringe):
                        tmp.neighbor4.gx = tmp.gx + tmp.neighbor4Cost
                        tmp.neighbor4.hx = self.hx(tmp.neighbor4, self.goal, self.weight)
                        tmp.neighbor4.fx = tmp.neighbor4.gx + tmp.neighbor4.hx
                        tmp.neighbor4.parent = tmp
                        self.push(fringe, tmp.neighbor4)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexW(fringe, tmp.neighbor4, tmp.neighbor4Cost, self.weight)
            if (tmp.neighbor5 != None):
                if (tmp.neighbor5 not in closed):
                    if (tmp.neighbor5 not in fringe):
                        tmp.neighbor5.gx = tmp.gx + tmp.neighbor5Cost
                        tmp.neighbor5.hx = self.hx(tmp.neighbor5, self.goal, self.weight)
                        tmp.neighbor5.fx = tmp.neighbor5.gx + tmp.neighbor5.hx
                        tmp.neighbor5.parent = tmp
                        self.push(fringe, tmp.neighbor5)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexW(fringe, tmp.neighbor5, tmp.neighbor5Cost, self.weight)
            if (tmp.neighbor6 != None):
                if (tmp.neighbor6 not in closed):
                    if (tmp.neighbor6 not in fringe):
                        tmp.neighbor6.gx = tmp.gx + tmp.neighbor6Cost
                        tmp.neighbor6.hx = self.hx(tmp.neighbor6, self.goal, self.weight)
                        tmp.neighbor6.fx = tmp.neighbor6.gx + tmp.neighbor6.hx
                        tmp.neighbor6.parent = tmp
                        self.push(fringe, tmp.neighbor6)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexW(fringe, tmp.neighbor6, tmp.neighbor6Cost, self.weight)
            if (tmp.neighbor7 != None):
                if (tmp.neighbor7 not in closed):
                    if (tmp.neighbor7 not in fringe):
                        tmp.neighbor7.gx = tmp.gx + tmp.neighbor7Cost
                        tmp.neighbor7.hx = self.hx(tmp.neighbor7, self.goal, self.weight)
                        tmp.neighbor7.fx = tmp.neighbor7.gx + tmp.neighbor7.hx
                        tmp.neighbor7.parent = tmp
                        self.push(fringe, tmp.neighbor7)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexW(fringe, tmp.neighbor7, tmp.neighbor7Cost, self.weight)
            if (tmp.neighbor8 != None):
                if (tmp.neighbor8 not in closed):
                    if (tmp.neighbor8 not in fringe):
                        tmp.neighbor8.gx = tmp.gx + tmp.neighbor8Cost
                        tmp.neighbor8.hx = self.hx(tmp.neighbor8, self.goal, self.weight)
                        tmp.neighbor8.fx = tmp.neighbor8.gx + tmp.neighbor8.hx
                        tmp.neighbor8.parent = tmp
                        self.push(fringe, tmp.neighbor8)
                        fringeEmpty = fringeEmpty + 1
                        nodesexpanded += 1
                    else:
                        self.UpdateVertexW(fringe, tmp.neighbor8, tmp.neighbor8Cost, self.weight)
