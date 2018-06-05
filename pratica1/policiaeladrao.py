#coding: utf-8

def backtracking(i, j):
				
	if(i >= 0 and i < 5 and j >= 0 and j < 5):
		
		global matrix
		global visitados
		
		if (matrix[i][j] == "0" and visitados[i][j] == False):
			
			visitados[i][j] = True
		
			backtracking(i, j + 1)
			backtracking(i + 1, j)
			backtracking(i, j - 1)
			backtracking(i - 1, j)

T = int(raw_input())

if (T >= 1 and T <= 400):

	for i in xrange(T):
		
		try:
			
			matrix = []
			
			while (len(matrix) < 5):
								
				line = raw_input().split()
				
				if (len(line) > 0):
					matrix.append(line)

			visitados = [[False for i in xrange(5)] for j in xrange(5)]
			
			backtracking(0, 0)
			
			if (visitados[4][4]):
				print "COPS"
			else:
				print "ROBBERS"
			
		except EOFError:
			break
