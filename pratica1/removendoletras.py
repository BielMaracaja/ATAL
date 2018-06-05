#coding: utf-8

sequencia = set()

def backtracking(palavra):
	
	global sequencia
	
	if len(palavra) <= 2:
		return;
	
	for i in xrange(len(palavra)):
		palavraAux = palavra[:i] + palavra[i+1:]
				
		lengthAux = len(sequencia)
		
		sequencia.add(palavraAux)
		
		if lengthAux < len(sequencia):
			backtracking(palavraAux)

while True:
	try:
		palavra = raw_input()

		sequencia = set()
			
		sequencia.add(palavra); sequencia |= set(palavra)
			
		backtracking(palavra)
		
		sequencia = list(sequencia)
		
		sequencia.sort()
			
		for string in sequencia:
			print string
		print
	except EOFError:
		break
