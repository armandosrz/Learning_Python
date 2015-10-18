import csv
from copy import copy
import AStarManhathan
import AStarMissplaced
from random import randint

def main():

	with open("a_star.csv", 'w') as csvf:
		write = csv.writer(csvf)
		write.writerow(['Sate', 'Manhathan States', 'Manhatan Moves', 'Missplaced States', 'Missplaced Moves'])
		for x in xrange(50):
			matrix = map(int,list("123456780"))
			matrixWithMoves = createMoves(matrix)
			manhathan = AStarManhathan.printSolutionManhatan(copy(matrixWithMoves))
			missplaced = AStarMissplaced.printSolutionMissplaced(copy(matrixWithMoves))
			state = ''.join(map(str, matrixWithMoves))
			write.writerow([state, manhathan[0], manhathan[1], missplaced[0], missplaced[1]])



def createMoves(matrix):
	for i in range(100):
		rand = randint(1,4)
		if rand == 1:
			AStarMissplaced.up(matrix, matrix.index(0))
		elif rand == 2:
			AStarMissplaced.down(matrix, matrix.index(0))
		elif rand == 3:
			AStarMissplaced.left(matrix, matrix.index(0))
		else:
			AStarMissplaced.right(matrix, matrix.index(0))
	return matrix

if __name__ == '__main__':
  main()
