class Node:
    def value(self):
        return self.Val

    def __init__(self):
        self.color=(255,255,255)
        self.block=False
        self.centerLeft=(0,0)
        self.centerTop=(0,0)
        self.centerRight=(0,0)
        self.centerBot=(0,0)
        self.topLeft=(0,0)
        self.hasRiver=False
        self.hardToTraverse=False