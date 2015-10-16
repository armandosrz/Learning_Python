import math
import sys
from PRIORITYQueue import PriorityQueue
from random import randint



# Program Starts

class State(object):

	def __init__(self, matrix, depth = 0, parent = None, h=0, g=0):
		self.parent = parent
		self.g = g
		self.h = h
		self.matrix = map(int, list(matrix))
		self.depth = depth
		self.f = g+h

	def __eq__(self, other):
		if isinstance(other, State):
			return self.matrix == other.matrix
	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return int(self.to_string())

	def __cmp__(self, other):
		return cmp(self.f, other.f)
	def __repr__(self):
		return self.__str__()
	def __str__(self):
		toPrint = ''
		for i, j in enumerate(self.matrix):
			toPrint += '{0:^3}|'.format(j)
			if i == 2 or i == 5:
				toPrint += '\n'
		return toPrint
	def to_string(self):
		return ''.join(map(str, self.matrix))

	def isGoal(self):
		goalStr = "123456780"
		goal = map(int, list(goalStr))
		if self.matrix == goal:
			return True
		else:
			return False
	def zeroIndex(self):
		return self.matrix.index(0)
	def getF(self):
		return self.h + self.g


def createStatesManhatan(current_state):
	children = []
	zeroPosition = current_state.zeroIndex()

	# Up
	newArray = up(current_state.matrix, zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = manhathanDistance(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Down
	newArray = down(current_state.matrix, zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = manhathanDistance(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Left
	newArray = left(current_state.matrix, zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = manhathanDistance(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Right
	newArray = right(current_state.matrix, zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = manhathanDistance(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)

	return children

def up(matrix, zeroIndex):
	if zeroIndex > 2:
		temp = matrix[zeroIndex]
		matrix[zeroIndex] = matrix[zeroIndex-3]
		matrix[zeroIndex-3] = temp
		return matrix
	else:
		return None

def down(matrix, zeroIndex):
	if zeroIndex < 6:
		temp = matrix[zeroIndex]
		matrix[zeroIndex] = matrix[zeroIndex+3]
		matrix[zeroIndex+3] = temp
		return matrix
	else:
		return None
def right(matrix, zeroIndex):
	if zeroIndex not in [2,5,8]:
		temp = matrix[zeroIndex]
		matrix[zeroIndex] = matrix[zeroIndex+1]
		matrix[zeroIndex+1] = temp
		return matrix
	else:
		return None
def left(matrix, zeroIndex):
	if zeroIndex not in [0,3,6]:
		temp = matrix[zeroIndex]
		matrix[zeroIndex] = matrix[zeroIndex+1]
		matrix[zeroIndex+1] = temp
		return matrix
	else:
		return None

def missplacedTitles(matrix):
	count = 0
	for i in xrange(len(matrix)):
		if (matrix[i] != i+1 and matrix[i] != 0):
			count += 1
	return count

def manhathanDistance(matrix):
	manhathan = 0
	goal = map(int, list("123456780"))
	for num in matrix:
		if num!=0:
			posMatrix = matrix.index(num)
			yMatrix, xMatrix = divmod(posMatrix, 3)
			posGoal = goal.index(num)
			yGoal, xGoal = divmod(posGoal, 3)
			manhathan += abs(yMatrix - yGoal) + abs(xMatrix - xGoal)
	return manhathan



def AStar():
	# Set up inital condition.
	# Ask for all requiered input.

	matrix = list("123456780")
	randmatrix = []
	for i in range(len(matrix)):
		index = randint(0, len(matrix)-1)
		randmatrix.append(int(matrix.pop(index)))
	m = map(int,list("123450786"))
	initialState = State(m)
	print initialState

	if initialState.isGoal():
		return initialState
	frontier = PriorityQueue()
	"""
		A set is an unordered data type with no repited elements.
		It is use for easy comparision of membership
	"""
	explored = set()
	frontier.enqueue(initialState)
	count  = 1
	while frontier:
		count += 1
		if (count == 50):
			break
		state = frontier.dequeue()
		explored.add(state)
		if state.isGoal():
			return state
		children = createStatesManhatan(state)
		for child in children:
			if (child not in explored) or (child not in frontier):
				frontier.enqueue(child)
			if child in explored:
				continue
			if child in frontier:
				if frontier.__getitem__(child).f > child.f:
					frontier.__delitem__(child)
					frontier.enqueue(child)
	for x in explored:
		print x.to_string()
		print
	return None


def printSolution(solution):

		path = []
		path.append(solution)
		parent = solution.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		pathSize = len(path)

		for i in range(pathSize):
			state = path[pathSize-i-1]
			print state
		print "Number of trips = " + str(pathSize-1)


def main():
	solution = AStar()
	print "A Star using manhathanDistance:"
	if solution is not None:
		#printSolution(solution)
		print "hey"
	else:
		print 'No solution.'


if __name__ == '__main__':
  main()
