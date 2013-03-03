import time


class Node:
    nodes = {}
    options = ((0,0,0,0), (0,1,0,1),(1,0,1,0), (1,1,1,0),(0,1,1,1),(1,0,1,1),(1,1,0,1), (1,1,1,1))
    @staticmethod
    def save( width, height):
        Rectangle.solutions[(width,height)].append( Rectangle(width, height, [[int(i) for i in n.state] for n in Node.nodes[(width,height)]]))

    def __init__(self, index, width, height):
        # [left, up, right, down]
        Node.nodes[(width,height)].append( self)
        self.width = width
        self.height = height
        self.index = index
        self.left = None
        self.up = None
        self.right = None
        self.down = None

        if self.index%(width+1) != 0: self.left = self.index - 1
        if self.index/(width+1) != 0: self.up = self.index - (width+1)
        if self.index%(width+1) != width: self.right = self.index + 1
        if self.index/(width+1) != height: self. down = self.index + (width+1)

        self.connections = [self.left, self.up, self.right, self.down]

        self.edge = False
        if None in self.connections:
            self.edge = True

        self.state = [c != None for c in self.connections]

        self.options = []

    def getOptions(self):
        left = Node.nodes[(self.width,self.height)][ self.left]
        up = Node.nodes[(self.width,self.height)][ self.up]

        if left.edge and up.edge:
            return Node.options[:]

        tmpOptions = []

        for o in Node.options:
            if left.edge or left.state[2] == o[0]:
                if up.edge or up.state[3] == o[1]:
                    tmpOptions.append( o)
        return tmpOptions

    def solve(self):
        self.options = self.getOptions()

        right = Node.nodes[(self.width,self.height)][ self.right]
        down = Node.nodes[(self.width,self.height)][ self.down]

        for o in self.options:
            self.state = list(o)
            # if neighbor is edge, set the value
            for i,c in enumerate(self.connections):
                if Node.nodes[(self.width,self.height)][ c].edge:
                    Node.nodes[(self.width,self.height)][ c].state[(i+2)%4] = self.state[i]
                    # if we're at the last node, save this config
            if right.edge and down.edge:
                Node.save( self.width, self.height)
            elif right.edge:
                Node.nodes[(self.width,self.height)][ self.right + 2].solve()
            else:
                right.solve()

	def __repr__(self):
		return "<Node {index} {connections}>".format(
											index=self.index,
											connections=self.connections)

class Box:
	def __init__(self, start, end):
		self.start = start
		self.size = (end[0] - start[0], end[1] - start[1])

	def __repr__(self):
		return "<Box {size} at {start}>".format(size=self.size, start=self.start)



class Rectangle:
	solutions = {}

	@staticmethod
	def solve(width, height):
		Rectangle.solutions[(width,height)] = []
		Node.nodes[(width,height)] = []

		size = (width+1)*(height+1)
		nodes = [Node(i,width,height) for i in range(size)]
		nodes[ width + 2].solve()


	def __init__(self, width, height, states):
		self.width = width
		self.height = height
		self.states = states
		self.boxes = self.getBoxes()
		self.stats = self.getStats()

	def getBoxes(self):
		boxes = []
		#self.visualize()
		for y in range( self.height):
			for x in range( self.width):
				index = y * (self.width+1) + x
				if self.states[ index][2] == 1 and self.states[ index][3] == 1:
					start = (x,y)
					pointer = [x+1,y+1]
					while pointer[0] <= self.width:
						tmpIndex = start[1] * (self.width+1) + pointer[0]
						if self.states[ tmpIndex][3] == 1:
							break
						pointer[0] += 1

					while pointer[1] <= self.height:
						tmpIndex = pointer[1] * (self.width+1) + pointer[0]
						if self.states[ tmpIndex][0] == 1 and self.states[ tmpIndex][1] == 1:
							break
						pointer[1] += 1

					boxes.append( Box( start, tuple(pointer)))
		return boxes

	def getStats(self):
		stats = {"total":len(self.boxes),
					"minX":min(self.boxes, key=lambda x: x.size[0]).size[0],
					"minY":min(self.boxes, key=lambda x: x.size[1]).size[1],
					"maxX":max(self.boxes, key=lambda x: x.size[0]).size[0],
					"maxY":max(self.boxes, key=lambda x: x.size[1]).size[1]}
		return stats

	def visualize(self):
		print self.states

	def __repr__(self):
		return "<Rectangle {width}x{height}>".format(
							width=self.width, height=self.height)
