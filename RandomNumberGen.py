import random
guesses=0
compNo = random.randint(0,21)
name=str(raw_input("What is your name?"))

print("Hello Mr."+name+"! Guess my number between 0&20. You got only 5 guesses! ")

while guesses<6:
	guesses=guesses+1
	print('Go '+str(guesses))
	guess=int(raw_input("Enter number:"))

	if guess==compNo:
		break
	else:
	   print('Wrong number.Guess again!')

if guess==compNo:
 print('You got it right at guess number '+str(guesses) )
if guess!=compNo:
 print('Sorry :( No more guesses left') 	   	