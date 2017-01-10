import random;
num = int(raw_input("Enter a random number between 1 to 100 = "));
num2 = random.randrange(100)+1;
guess=1;	
while num != num2:
	if num < num2 : 
		num = int(raw_input("your guess is too low, Guess again = "));
#		num = int(raw_input("Enter a random number between 1 to 100"));
	elif num > num2:
		num = int(raw_input("your guess is too high, Guess again = "));
#                num = int(raw_input("Enter a random number between 1 to 100"));
	#else:	
	#	print("Congrats, your guess is right...!!")
	guess+=1;

print("Congrats, your guess is right...!!");
print ("You took"),
print( guess), 
print("chances to guess the right answer"); 
