import random;
HANGMAN = (
"""
	----
       |   |
       |
       |
       |
       |
       |
       |
       |
       |
    ________

""" ,
"""
        ----
       |   |
       |   0
       |
       |
       |
       |
       |
       |
       |
    ________

""" ,
"""
        ----
       |   |
       |   0
       |  -+-
       |
       |
       |
       |
       |
       |
    ________

""" ,
"""
        ----
       |   |
       |   0
       | /-+-
       |
       |
       |
       |
       |
       |
    ________

""" ,
"""
        ----
       |   |
       |   0
       | /-+-/
       |
       |
       |
       |
       |
       |
    ________

""" ,
"""
        ----
       |   |
       |   0
       | /-+-/
       |   |
       |
       |
       |
       |
       |
    ________

""" ,
"""
        ----
       |   |
       |   0
       | /-+-/
       |   |
       |   |
       |   |
       |   
       |
       |
    ________

""" ,
"""
        ----
       |   |
       |   0
       | /-+-/
       |   |
       |   |
       |   |
       |  | |
       |  | |
       |
    ________

""" )

MAX_WRONG = len(HANGMAN)-1;
WORDS = ("APPLE","ORANGES", "ORANGE","PEACH" , "WATERMELON");
word = random.choice(WORDS);
so_far = "-"*len(word);
wrong = 0;
used= [];

print("\t\tWelcom to HANGMAN..Good Luck!!");

while wrong < MAX_WRONG and so_far!=word:
	print (HANGMAN[wrong]);
	print ("\nYou have used the following letter");
	print"\nSo far the word is : ", so_far;
	
	guess = raw_input("Enter the guessed letter = ");
	guess = guess.upper();
	
	while guess in used:
		print ("Letter has been used");
                guess = raw_input("Enter the guessed letter = ");
		guess = guess.upper();
	used.append(guess);
	if guess in word :
		print "\n Yes ", guess," is in the word";

		new = "";
		for i in range(len(word)):
			if guess == word[i]:
				new+=guess;
			else : 
				new+=so_far[i];
		so_far = new;
	else : 
		print"\n Sorry, ",guess, " is not in the word";
		wrong += 1;
if wrong == MAX_WRONG:
	print (HANGMAN[wrong]);
	print ("\n you have benn hanged..!!");
else : 
	print ("\nYou guessed it");
print"\n The word was", word;

