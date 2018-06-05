#coding: utf-8

def validate(s):
	for i in xrange(1, len(s)/2+1):
		
		if (s[-i-i:-i] == s[-i:]):
			return True
	
	return False

def generatecode(s, l):
	
	if (not validate(s)):
		r = ''
		
		if (len(s) < l):
			r = generatecode(s + 'N', l)
		
			if (r != ''):
				return r
			
			r = generatecode(s + 'O', l)

			if (r != ''):
				return r
			
			r = generatecode(s + 'P', l)

			if (r != ''):
				return r
			
			return ''
		
		else: 
			return s
	else:
		return ''

s = ''
a = ''

for i in range(1,7):
	s = generatecode(a, 995 * i)
	a = s

while True:
	try:
		n = int(raw_input())

		if (n == 0):
			break
		
		print s[:n]
	
	except EOFError:
		break
