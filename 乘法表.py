for i in range(1,10):
	for j in range(1,10):
		z='{0:1}x{1:1}={2:<2}'.format(i,j,i*j)
		if i>j:
			print(end='       ')
		else:
			print(z,end=' ')
	print()
