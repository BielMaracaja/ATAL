#coding: utf-8

def combinations(n, c1, c2, c3):
	sequencia = set()
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			for k in range(1, n + 1):
				total = (i * c1) + (j * c2) + (k * c3)
				sequencia.add(total)
	
	return len(sequencia)

while True:
	try:
		N, M = map(int, raw_input().split())
		
		C = map(int, raw_input().split())
		
		if(N == 1):
			total = combinations(M, C[0], 0, 0)
		if(N == 2):
			total = combinations(M, C[0], C[1], 0)
		if(N == 3):
			total = combinations(M, C[0], C[1], C[2])
		
		if (total == M ** N):
			print "Lucky Denis!"
		else:
			print "Try again later, Denis..."
		
	except EOFError:
		break

