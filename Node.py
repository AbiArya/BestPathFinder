class Node:
    def value(self):
        return self.Val

    def __init__(self):
        self.color=(255,255,255)
        self.block=False
        self.hasRiver=False
        self.hardToTraverse=False
        self.start=False
        self.finish=False
        self.centerLeft = (0, 0)
        self.centerTop = (0, 0)
        self.centerRight = (0, 0)
        self.centerBot = (0, 0)
        self.topLeft = (0, 0)
        self.fx = 0;
        self.gx = 0
        self.neighbor1 = None;
        self.neighbor1Cost = 0;
        self.neighbor2 = None;
        self.neighbor2Cost = 0;
        self.neighbor3 = None;
        self.neighbor3Cost = 0;
        self.neighbor4 = None;
        self.neighbor4Cost = 0;
        self.neighbor5 = None;
        self.neighbor5Cost = 0;
        self.neighbor6 = None;
        self.neighbor6Cost = 0;
        self.neighbor7 = None;
        self.neighbor7Cost = 0;
        self.neighbor8 = None;
        self.neighbor8Cost = 0;
        self.parent = None;
        self.parentToCurrent = 0;
        self.index = 0;
        self.x = 0;
        self.y = 0;