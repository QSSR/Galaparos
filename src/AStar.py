'''
This file contains the A* algorithm that will be used by lab3.py. lab3.py imports this function
'''

import math
import numpy
import sys


# A* navigation class
#based on pseudocode in wikpedia
class AStar:

    openSet = 0  #set of tentative nodes to be evaluated, initially containing the start node
    closedSet = 0 #set of nodes already evaluated
    mapArray = 0 
    nodesArray = 0
    size = 0
    
    def __init__ (self, mapMsg):

        self.mapArray = [] 

        # convert the data from the message into an array
        for q in mapMsg.data:
            self.mapArray.append(q)

        # set size
        self.size = [mapMsg.info.width, mapMsg.info.height]

        # convert the map array into a 2D array
        self.mapArray = self.rectangularizeMap(self.mapArray, self.size)

        # convert ints in mapArray to nodes
        self.nodesArray = self.toNodes(self.mapArray)

        return

    # navigate from one point to another
    def navigate(self, begin, goal):

        # the set of nodes already evaluated starts empty
        self.closedSet = []

        # the set of nodes to be evaluated starts with the start node
        self.openSet = [self.nodesArray[begin[1]][begin[0]]]

        # define the start nodes scores
        self.openSet[0].gScore = 0 #cost from start along best known path
        self.openSet[0].hScore = self.hScore(begin, goal) 
        self.openSet[0].fScore = self.openSet[0].hScore + self.openSet[0].gScore

        # while there are still nodes in the open set to be evaluated
        while len(self.openSet) > 0: #open set is not empty

            # the current node is the node in the open set with the lowest F Score
            current = self.openSet.pop(0)

            # if the current node is the goal, reconstruct the path from the goal
            if current.pos[0] is goal[0] and current.pos[1] is goal[1]:

                return self.reconPath(current)

            # insert the current node into the closed set
            self.closedSet.append(current)

            # evaluate all of the current node's neighbors
            for n in current.neighbors:

                # if the current neighbor has been evaluated, skip this neighbor
                if self.closedSet.count(n) > 0:
                    continue

                # create a tentative G Score
                tGScore = current.gScore + self.dist(current.pos, n.pos)
			#length of this path

                # if this neighbor has not been evaluated yet or if the tentative G score is better 

                if self.openSet.count(n) is 0 or tGScore < n.gScore:

                    # update the scores
                    n.cameFrom = current
                    n.gScore = tGScore
                    n.hScore = self.hScore(n.pos, goal)
                    n.fScore = n.gScore + n.hScore

                    # add this neighbor to the open set if it is not already there
                    if self.openSet.count(n) is 0:

                        self.openSet.append(n)

                        # sort the open set by the F Score so that the lowest score is at the start
                        self.openSet.sort(key=lambda x: x.fScore, reverse=False)

        # if the open set has been depleted, there is no solution
        return False
    
    # The heuristic function, in this case is octo-directional distance, but it can be anything
    # choose what's most appropriate for the robot's navigation capability
    def hScore (self, start, end):

        a = start[0] - end[0]
        b = start[1] - end[1]
    
        return abs(a - b) + (2**0.5)*min(abs(a),abs(b))
    
    # absolute distance    
    def dist (self, start, end):

        a = start[0] - end[0]
        b = start[1] - end[1]
        
        return (a**2 + b**2)**0.5
    
    # reconstruct path starting from the end    
    def reconPath (self, end):

        path = [end]

        current = path[0]

        # until the start is reached, iterate by adding the current node to the path list
        # then replace the current node with the node that led to the previous node
        while current.cameFrom is not 0:
            path.append(current.cameFrom)
            current = current.cameFrom
    
        return path

    # convert a 1D array of a grid to a 2D array
    def rectangularizeMap(self, mArray, size):
        newMap = mArray[0:size[0]]

        newMap = [newMap]

        i = 1
        while i < size[1]:

            newMap.append(mArray[size[0]*i:size[0]*(i+1)])

            i += 1

        return newMap

    # convert a 2D array of ints to a 2D array of nodes
    def toNodes(self, mArray):

        i = 0
        j = 0

        for q in mArray:
            i = 0
            for r in q:
                mArray[j][i] = ANode(r, i, j)
                i += 1
            j += 1

        j = 0
        while j < len(mArray):
            i = 0
            while i < len(mArray[0]):
                mArray[i][j].neighbors = self.getNeighbors(mArray[i][j])
                i += 1
            j += 1

        return mArray

    # return an array of neighboring nodes of a given node
    def getNeighbors(self, node):
        neighbors = []

        j = -1
        while j <= 1 and node.pos[1] + j < self.size[1] and node.pos[1] + j >= 0:
            i = -1
            while i <= 1 and node.pos[0] + i < self.size[0] and node.pos[0] + i >= 0:

                if j is 0 and i is 0:
                    a = 1
                else:
                    if self.mapArray[j+node.pos[1]][i+node.pos[0]].cost is 0:
                        neighbors.append(self.mapArray[j+node.pos[1]][i+node.pos[0]])
                i += 1
            j += 1

        return neighbors

# node class used by AStar
class ANode:
    pos = 0
    gScore = -1
    hScore = -1
    fScore = -1
    neighbors = 0
    cameFrom = 0

    def __str__ (self):
		return "{" + str(self.pos) + " " + str(self.fScore) + "}"

    def __repr__ (self):
		return "{" + str(self.pos) + " " + str(self.fScore) + "}"


