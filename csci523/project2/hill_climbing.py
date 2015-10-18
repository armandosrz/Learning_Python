from State import State
from AStarManhathan import up, down, left, right, createMoves, manhathanDistance
from copy import copy

def createStatesManhatan(current_state):
	children = []
	zeroPosition = current_state.zeroIndex()
	mtrx = current_state.getMatrix()
	# Up
	newArray = up(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.f = manhathanDistance(newArray)
		children.append(newState)
	# Down
	newArray = down(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.f = manhathanDistance(newArray)
		children.append(newState)
	# Left
	newArray = left(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.f = manhathanDistance(newArray)
		children.append(newState)
	# Right
	newArray = right(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.f = manhathanDistance(newArray)
		children.append(newState)

	return children

def hillClimbing(matrix):
	# Set up inital condition.
	# Ask for all requiered input.
	global statesCount
	"""
	matrix = map(int,list("123456780"))
	print matrix
	test = map(int, list("704512836"))
	matrixWithMoves = createMoves(matrix)
	print test
	"""
	currentState = State(matrix)
	currentState.f = manhathanDistance(matrix)
	nextState = State(matrix)
	nextState.f = copy(currentState.f)
	statesCount = 1

	while True:
		children = createStatesManhatan(currentState)
		for child in children:
			if child.f < nextState.f:
				nextState = child
		if nextState.f >= currentState.f:
			if nextState.isGoal():
				return "Goal", nextState, statesCount
			else:
				return 'Local Maxima', nextState, statesCount
		currentState = copy(nextState)
		statesCount += 1
	return None

def printSolutionHillClimbing(matrix):
	solution = hillClimbing(matrix)
	if not None:
		print solution[0]
		print solution[1]
		print solution[2]
	else:
		print 'No solution'


def main():
	printSolutionHillClimbing(createMoves(map(int, list("123456780"))))


if __name__ == '__main__':
  main()
