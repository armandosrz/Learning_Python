from State import State
from AStarManhathan import up, down, left, rigth

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

def HillClimbing(matrix):
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
	initialState = State(matrix)
	initialState.f = manhathanDistance(matrix)


	if initialState.isGoal():
		return initialState
	frontier = PriorityQueue()
	explored = {}
	frontier.enqueue(initialState)
	statesCount  = 1
	while frontier:
		state = frontier.dequeue()
		#print state.to_string() + " " + str(state.f)
		explored[state.to_string()] = 1
		if state.isGoal():
			return state
		children = createStatesManhatan(state)
		for child in children:
			if child.to_string() in explored:
				continue
			if child not in frontier:
				frontier.enqueue(child)
				statesCount += 1
			else:
				ch = frontier.__getitem__(child)
				if ch.f > child.f:
					#print child.to_string() + " " + str(ch.f) + " " + str(child.f)
					frontier.__delitem__(child)
					frontier.enqueue(child)
					ts = frontier.__getitem__(child)
	return None


def main():
	printSolutionManhatan(createMoves(map(int, list("123456780"))))


if __name__ == '__main__':
  main()
