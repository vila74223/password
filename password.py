i = 3
while i > 0:
	i = i - 1
	p = input('Please enter your password: ')
	if p == 'a123456':
		print('Logged in')
		break
	else:
		print('Wrong password! You have', i, 'chances' )
	
		
		

