class square():
	def __init__(self,interface):
	self.posX
	self.posY
	self.D = 0
	self.state 0 #0 is unchecked, 1 is checked, 2 is wall
	self.children[] #0-4 places it can go
	def getCell():
		cells = GridCells()
		modX = self.posX % cells.cell_width
		modY = self.posY % cells.cell_width
		i = self.posX / cells.cell_width
		j = self.posY / cells.cell_height
		if modX != 0:
			i++
		if modY != 0:
			j++
		point =Point()
		point.x = i
		point.y = j
		point.z = 0
		return point

def Search(start):

def neighbor_nodes(pos):
	children[1] = findN`ode(posX, posY+1)
	children[2] = findNode(posX+1,posY)
	children[1] = findNode(posX, posY-1)
	children[2] = findNode(posX-1,posY)
	pos.children[] = neighbors[]
		
def stateCheck(pos):
	
def distCheck(start, end):
	distX = end.posX - start.posX
	distY = end.posY - start.posY
	dist = sqrt((distX^2) + (distY^2))
	start.D = dist

def updateGrid(pos):
	for i in pos.children.size():
		if pos.children[i].state = 1:
			#paint them the color blue
			pos.children[i].getCell().color = (255,0,0) 
		if pos.children[i].state = 2:
			#paint them the color black
			pos.children[i].getCell().color = (255,255,255)
		else:
			pos.children[i].getCell().color = (0,0,0) 