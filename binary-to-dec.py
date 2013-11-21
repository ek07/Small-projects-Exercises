# Converts a binary number to decimal and vice versa
import math

option = input("Press 1 enter a binary(to decimal) or 2 to enter a decimal(to binary): ")
num = str(input("Please enter your number: "))

if option==1:
	i = len(num)
	exponent = 0
	dec_rep=0
	
	while i>0:
		dec_rep+=int(num[i-1]) * math.pow(2, exponent)
		i -=1
		exponent+=1
	
	print int(dec_rep)
	
elif (option==2):
	num = int(num)
	out=0
	length=1
	
	while num > length:
		length *=2
	
	length/=2
	num -= length
	out+=1
		
	while num!=0:
		out*=10
		if num >= length/2:
			num-= length/2
			out +=1
			
		length=length/2
		
	print out
			
	
elif option==-1:
	print "Exiting..."
	
else:
	print "Please enter either 1 or 2 or -1(to exit): "
	
