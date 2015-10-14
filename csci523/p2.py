import math
import sys


# Program Starts

class State():
	def __init__(self, canLeft, misLeft, ship, canRight, misRight):
		self.canLeft = canLeft
		self.misLeft = misLeft
		self.ship = ship
		self.canRight = canRight
		self.misRight = misRight
		self.parent = None  #Pointer to parent state Generated


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

	def __hash__(self):
		return hash((self.canLeft, self.misLeft, self.ship, self.canRight, self.misRight))

	def __eq__(self, other):
		return (self.canLeft == other.canLeft) and (self.misLeft == other.misLeft)\
					and (self.ship == other.ship) and (self.canRight == other.canRight)\
					and (self.misRight == other.misRight)
	def __str__(self):
		return "(" + str(self.canLeft) + "," + str(self.misLeft) \
						+ "," + self.ship + "," + str(self.canRight) + "," + \
						str(self.misRight) + ")"




def BFS():
	global shipCount #Capacity of the boat
	global generatedStates #Num of total states Generated.

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
