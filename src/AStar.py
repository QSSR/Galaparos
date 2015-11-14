
class grid():
	def__init__(self):
	cells = gridCells()
	width = data.info.width / cells.cell_width
        height = data.info.height / cells.cell_height
	self.map[width,height]

#set Start Point at 0,0
global start = square()
start.posX = 0
start.posY = 0
start.D = distCheck(start)



class square():
	def __init__(self):
	self.posX
	self.posY
	self.D = 0
	self.state 0 #0 is unchecked, 1 is checked, 2 is wall
	self.children[4] #0-4 places it can go
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

def neighbor_nodes(pos):
	children[1] = grid.findNode(posX, posY+1)
	children[2] = grid.findNode(posX+1,posY)
	children[1] = grid.findNode(posX, posY-1)
	children[2] = grid.findNode(posX-1,posY)
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
			pos.children[i].getCell().color = (0,0,0)
		else:
			pos.children[i].getCell().color = (255,255,255) 

def end(pos):
	count
    pos.checkOpts()
    for i in pos.children.size():
		if pos.children[i] == null:
			count++
	if count == 4:
		if pos = grid.finish:
			return path
		else:
			nextOpt(start)	
			

def reset(map):
    map.shape[1] = row_range
    map.shape[2] = col_range
	for i <= col_range:
		for j <= row_range:
			map[i,j].state = 0;
			map[i,j].getCell().color = (255,255,255)

