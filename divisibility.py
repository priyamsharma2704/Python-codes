#print ("\a");
x= raw_input("Enter 1st number = ")
y = raw_input("Enter 2nd number = ")
#x=4

#y=12
if (int(x)%int(y) == 0):
	print("x is divisible by y")
elif (int(y)%int(x) == 0):
	print ("y is divisble by x")
else:
	print (" not divisible")

