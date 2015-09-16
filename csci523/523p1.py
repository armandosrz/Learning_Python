import math

#______________________________________________________________________________
# Queues: FIFOQueue (source: http://aima-python.googlecode.com/svn/trunk/utils.py)

class Queue:
    """Queue is an abstract class/interface.
    Supports the following methods and functions:
        q.append(item)  -- add an item to the queue
        q.extend(items) -- equivalent to: for item in items: q.append(item)
        q.pop()         -- return the top item from the queue
        len(q)          -- number of items in q (also q.__len())
        item in q       -- does q contain item?
    If Python ever gets interfaces, Queue will be an interface."""

    def __init__(self):
        abstract

    def extend(self, items):
        for item in items: self.append(item)

class FIFOQueue(Queue):
    """A First-In-First-Out Queue."""
    def __init__(self):
        self.A = []; self.start = 0
    def enqueue(self, item):
        self.A.append(item)
    def __len__(self):
        return len(self.A) - self.start
    def extend(self, items):
        self.A.extend(items)
    def dequeue(self):
        e = self.A[self.start]
        self.start += 1
        if self.start > 5 and self.start > len(self.A)/2:
            self.A = self.A[self.start:]
            self.start = 0
        return e
    def __contains__(self, item):
        return item in self.A[self.start:]

# Program Starts

class State():
	def __init__(self, canLeft, misLeft, ship, canRight, misRight):
		self.canLeft = canLeft
		self.misLeft = misLeft
		self.ship = ship
		self.canRight = canRight
		self.misRight = misRight
		self.parent = None


	""" The python parser reads logical lines which are terminated when a new
		line is encountered. It is like the ';' in java. Whenever you have a long
		logical line that you want to split in two for readability pourposes
		you can use the backslash character, just like in the function below.
	"""

	def isValid(self):
		if self.misLeft >= 0 and self.misRight >= 0 \
                   and self.canLeft >= 0 and self.canRight >= 0 \
                   and (self.misLeft == 0 or self.misLeft >= self.canLeft) \
                   and (self.misRight == 0 or self.misRight >= self.canRight):
			return True
		else:
			return False

	def isGoal(self):
		if self.misLeft == 0 and self.canLeft == 0:
			return True
		else:
			return False

def createStates(current_state):
	children = [];
	if current_state.ship == 'left':
		# Two Missionaries to the rigth
		newState = State(current_state.canLeft, current_state.misLeft-2, 'rigth',
						current_state.canRight, current_state.misRight+2)
		if newState.isValid():
			newState.parent = current_state
			children.append(newState)
		# Two Cannibals to the rigth
		newState = State(current_state.canLeft-2, current_state.misLeft, 'rigth',
						current_state.canRight+2, current_state.misRight)
		if newState.isValid():
			newState.parent = current_state
			children.append(newState)
		# One Cannibal and one Missionary to the rigth
		newState = State(current_state.canLeft-1, current_state.misLeft-1, 'rigth',
						current_state.canRight+1, current_state.misRight+1)
		if newState.isValid():
			newState.parent = current_state
			children.append(newState)
		# One Missionary to the rigth
		newState = State(current_state.canLeft, current_state.misLeft-1, 'rigth',
						current_state.canRight, current_state.misRight+1)
		if newState.isValid():
			newState.parent = current_state
			children.append(newState)
		# One Cannibal to the rigth
		newState = State(current_state.canLeft-1, current_state.misLeft, 'rigth',
						current_state.canRight+1, current_state.misRight)
		if newState.isValid():
			newState.parent = current_state
			children.append(newState)
	else:
		# Two Missionaries to the rigth
		newState = State(current_state.canLeft, current_state.misLeft+2, 'left',
						current_state.canRight, current_state.misRight-2)
		if newState.isValid():
			newState.parent = current_state
			children.append(newState)
		# Two Cannibals to the left
		newState = State(current_state.canLeft+2, current_state.misLeft, 'left',
						current_state.canRight-2, current_state.misRight)
		if newState.isValid():
			newState.parent = current_state
			children.append(newState)
		# One Cannibal and one Missionary to the left
		newState = State(current_state.canLeft+1, current_state.misLeft+1, 'left',
						current_state.canRight-1, current_state.misRight-1)
		if newState.isValid():
			newState.parent = current_state
			children.append(newState)
		# One Missionary to the rigth
		newState = State(current_state.canLeft, current_state.misLeft+1, 'left',
						current_state.canRight, current_state.misRight-1)
		if newState.isValid():
			newState.parent = current_state
			children.append(newState)
		# One Cannibal to the rigth
		newState = State(current_state.canLeft+1, current_state.misLeft, 'left',
						current_state.canRight-1, current_state.misRight)
		if newState.isValid():
			newState.parent = current_state
			children.append(newState)
	return children

def BFS():
	# Set up inital condition. 3 Cannibals and Missionaries on the left
	CannibalsStart = input("Enter number of cannibals: ")
	initialState = State(CannibalsStart,CannibalsStart,'left',0, 0)
	if initialState.isGoal():
		return initialState
	frontier = FIFOQueue()
	"""
		A set is an unordered data type with no repited elements.
		It always for easy comparision of membership
	"""
	explored = set()
	frontier.enqueue(initialState)
	while frontier:
		state = frontier.dequeue()
		explored.add(state)
		children = createStates(state)
		for child in children:
			if (child not in explored) or (child not in frontier):
				if state.isGoal():
					return state
				frontier.enqueue(child)
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
		print "Number of states = " + str(pathSize-1)

def main():
	solution = BFS()
	print "Missionaries and Cannibals solution:"
	print "(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)"
	printSolution(solution)

if __name__ == '__main__':
  main()