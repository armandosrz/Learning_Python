CSCI 531: Artificial Intelligence
Section 1
Javier Armando Suarez Rivas

			Program 2: 8 Puzzle Sliding Titles

Language: Python
Run: python (name of class.py)

Data Structure/State Representation:
		State.py:
		The state was represented with a python class named State() which includes
		pointer to the parent state (null in case of root) and several variables
		that contain integer and string values to represent the current state of
		the program like g, h, f, and the matrix representation. In other words
		my state consist of a pointer to the parent node, a matrix, and 4 int values.
		Methods:
			-isValid(): Checks is the generated state is a valid one within the
									parameter of our program.
			-isGoal(): Check is the state is equal to the goal state which is hard-coded
								 to match "123456780".
			-__hash__(): Overwrites the python class hash to generate a unique hash
									 number, which will be the same in case of repeated state.
			-__eq__(): compares if two State() objects are equal based on the actual
								 matrix values.
			-__cmp__(): Overwrites the python compare function to the evaluate f value
									of each node, this method is used to determine the order of
									the Priority Queue.

		PRIORITYQueue.py:
		The PriorityQueue class was obtained from an on-line library. It acts as an
		expected PriorityQueue would.
				http://aima-python.googlecode.com/svn/trunk/utils.py

		AStarManhathan.py:
		This file contains the necessary methods to generate all possible movements
		form a specific state, calculation its respective heuristic functions
		(based on the Manhattan heuristic) and returning those values to the
		main AStar() function. Which uses a map to keep track of explored states
		and a priority queue to find the solution.
			The print solution function grabs the solution state and iterates all
		the way until the initial state to determine the path and the length a
		the solution from the start node.

		AStarMissplaced.py:
		Same as above, but with the adapted to hold the misplaced titles heuristic.

		hill_climbing.py:
		This file contains the three different hill climbing algorithms implementations,
		which are: steepest, first choice, and random restart.
			-Steepest: In this algorithm we select the node with the smaller heuristic
			value from all possible children as our next node. The process keeps going
			until a plateau or goal is reached.
			-First Choice: the first choice algorithm, which was deterministically
			implemented, selects the first node with a heuristic function smaller than
			the current, without considering all other neighbor nodes.
			-Random Restart: For this implementation, I decided to randomly generate
			20 more moves and re-run the algorithm until a solution is reached.
			Which makes my code complete, since a solution is always reached, but at
			the expense of performance.



Issues encountered:
		Just the usual debugging problems, like infinite loops and arithmetic
		errors in my logic statements.
		Ignorance of python language class implementation for object comparison,
		which was solved with the __hash__() and __eq__() function additions inside
		of the State() class. My elements in the explored set were all being added
		to the set, even if the objects hold the same information.

Known bugs:
	At running time the program will display a syntax warning:
		'SyntaxWarning: name 'generatedStates' is used prior to global declaration'
	This does not affect the performance of the program. I am still learning
	about globals in python.
	Some of the special cases come out with no solution even though Wikipedia
	says it should be one. This part was not required for undergrads

Extra:
	My program generates and displays a graph of the generated States and the
	connection with parent and sons states.
