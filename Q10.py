Y=int(input('Enter year'))
if Y<0:
	print('invalid')
else:
	if(Y%400==0):
		print("it is a leap year")
	else:
		if(Y%100==0):
			print('it is not a leap year')
		else:
			if(Y%4==0):
				print('it is a leap year')
			else:
					print('it is not a leap year')