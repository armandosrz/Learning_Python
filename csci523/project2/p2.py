import math
import sys
from FIFOQueue import FifoQueue


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

	def __hash__(self):
		return hash(tuple(self.matrix))

	def __cmp__(self, other):
		return cmp(self.f, other.f)

	def __str__(self):
		print = ''
		for i, j in enumerate(self.matrix):
			print += '{0:^3}|'.format(j)
			if i == 2 or i == 5:
				print += '\n'
		return print
	def isGoal(self):
		goalStr = "123456780"
		goal = map(int, list(goalStr))
		if self.matrix == goal:
			return True
		else:
			return False
	def zeroIndex(self):
		return self.matrix.index(0)
	def getF():
		return self.h + self.g


def createStatesManhatan(current_state):
	children = []
	zeroPosition = current_state.zeroIndex()

	# Up
	newArray = up(current_state.matrix, zeroPosition)
	if newArray not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = manhathanDistance(matrix)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Down
	newArray = down(current_state.matrix, zeroPosition)
	if newArray not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = manhathanDistance(matrix)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Left
	newArray = left(current_state.matrix, zeroPosition)
	if newArray not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = manhathanDistance(matrix)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Right
	newArray = right(current_state.matrix, zeroPosition)
	if newArray not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = manhathanDistance(matrix)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)

	return children

def up(matrix, zeroIndex):
	if zeroIndex > 2:
		temp = matrix[z]
		matrix[z] = matrix[z-3]
		matrix[z-3] = temp
		return matrix
	else:
		return None

def down(matrix, zeroIndex):
	if zeroIndex < 6:
		temp = matrix[z]
		matrix[z] = matrix[z+3]
		matrix[z+3] = temp
		return matrix
	else:
		return None
def right(matrix, zeroIndex):
	if zeroIndex < not in [2,5,8]:
		temp = matrix[z]
		matrix[z] = matrix[z+1]
		matrix[z+1] = temp
		return matrix
	else:
		return None
def left(matrix, zeroIndex):
	if zeroIndex < not in [0,3,6]:
		temp = matrix[z]
		matrix[z] = matrix[z+1]
		matrix[z+1] = temp
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
			manhathan += abs(yMatrix - yGoal) + abs(xMatrix, xGoal)
	return manhathan

def AStar():


	# Set up inital condition.
	# Ask for all requiered input.
	print "Enter cannibals and Missionaries separated by commas (3,3): "
	items = [x for x in raw_input().split(',')]
	shipCount = int(raw_input('Enter number of seats on the boat: '))
	generatedStatesLimit = int(raw_input('Enter Limit num of generatedStates: '))
	generatedStates = 1
	initialState = State(int(items[0]),int(items[1]),'left',0, 0)

	if initialState.isGoal():
		return initialState
	frontier = FIFOQueue()
	"""
		A set is an unordered data type with no repited elements.
		It is use for easy comparision of membership
	"""
	explored = set()
	frontier.enqueue(initialState)

	while frontier:
		state = frontier.dequeue()
		explored.add(state)
		children = createStates(state)
		for child in children:
			if (child not in explored) or (child in frontier):
				if child.isGoal():
					return child
				frontier.enqueue(child)
		if generatedStatesLimit < generatedStates:
			print('States Limit reached.')
			sys.exit()
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
			print "(" + str(state.canLeft) + "," + str(state.misLeft) \
							  + "," + state.ship + "," + str(state.canRight) + "," + \
							  str(state.misRight) + ")"
		print "Number of trips = " + str(pathSize-1)


def main():
	solution = BFS()
	print "Missionaries and Cannibals solution:"
	print "(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)"
	if solution is not None:
		printSolution(solution)
	else:
		print 'No solution.'
	print "Number of nodes generated: " + str(generatedStates)

if __name__ == '__main__':
  main()
