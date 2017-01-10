num = int(raw_input("Enter the number between 1 and 3 = "));
if num == 1:
	for i in range(2,10):
		print('num = '+ str(i))

elif num == 2:
	for j in range(1,11,3):
		print("num = " + str(j))
elif num == 3:
	name = raw_input("Enter your name = ");
	high = len(name);
	low = 0;
	for i in range(low,high):
		print("word["),
		print(i),
		print("] is = "),
		print(name[i]);

