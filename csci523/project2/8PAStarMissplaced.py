from PRIORITYQueue import PriorityQueue
from random import randint
from State import State


# Program Starts
def createStatesMissplaced(current_state):
	children = []
	zeroPosition = current_state.zeroIndex()

	# Up
	newArray = up(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, \
				   parent = current_state)
		newState.h = missplacedTitles(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Down
	newArray = down(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, \
				   parent = current_state)
		newState.h = missplacedTitles(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Left
	newArray = left(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = missplacedTitles(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Right
	newArray = right(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = missplacedTitles(newArray)
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
		#print matrix
		return matrix
	else:
		return None
def left(matrix, zeroIndex):
	if zeroIndex not in [0,3,6]:
		temp = matrix[zeroIndex]
		matrix[zeroIndex] = matrix[zeroIndex-1]
		matrix[zeroIndex-1] = temp
		return matrix
	else:
		return None

def missplacedTitles(matrix):
	count = 0
	for i in xrange(len(matrix)):
		if matrix[i] != i+1 and matrix[i] != 0:
			count += 1
	return count

def createMoves(matrix):
	for i in range(100):
		rand = randint(1, 4)
		if rand == 1:
			up(matrix, matrix.index(0))
		elif rand == 2:
			down(matrix, matrix.index(0))
		elif rand == 3:
			left(matrix, matrix.index(0))
		else:
			right(matrix, matrix.index(0))
	return matrix



def AStar():

	# Set up inital condition.
	# Ask for all requiered input.
	global statesCount
	statesCount = 1
	matrix = map(int,list("123456780"))
	print matrix
	matrixWithMoves = createMoves(matrix)
	print matrixWithMoves
	initialState = State(matrixWithMoves)
	initialState.f = missplacedTitles(matrixWithMoves)


	if initialState.isGoal():
		return initialState
	frontier = PriorityQueue()
	explored = {}
	frontier.enqueue(initialState)
	while frontier:
		state = frontier.dequeue()
		explored[state.to_string()] = 1
		if state.isGoal():
			return state
		children = createStatesMissplaced(state)
		for child in children:
			if child.to_string() in explored:
				continue
			if child not in frontier:
				frontier.enqueue(child)
				statesCount += 1
			else:
				ch = frontier.__getitem__(child)
				if ch.f > child.f:
					frontier.__delitem__(child)
					frontier.enqueue(child)
					ts = frontier.__getitem__(child)
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
		if i < pathSize-1:
			print "-----> " + u"\u2193"
		else:
			print u"\u2191"*5
	print "Number of states added to Queue = " + str(statesCount)
	print "Number of trips = " + str(pathSize-1)



def main():
	solution = AStar()
	print "A Star using missplacedTitles:"
	if solution is not None:
		printSolution(solution)
		print "We made it :)"
	else:
		print 'No solution.'


if __name__ == '__main__':
	main()
