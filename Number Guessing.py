from random import randint
from math import ceil
from os import system, name
from sys import exit

def Menu(Input):
	Number = {
		1 : 10,
		2 : 50,
		3 : 100,
		4 : 150,
		5 : 200	
	}
	RandomNumber = randint(1, Number[Input])
	return RandomNumber, Number[Input]

def CheckNumber(UserGuess, Number, RandRange):
	UserGuess = int(UserGuess)

	if UserGuess < Number:
		print('\nYour Guess too Little.')
		return False

	elif UserGuess > Number and UserGuess <= RandRange:
		print('\nYour Guess too Big.')
		return False

	elif UserGuess == Number:
		print('\nYou Won!\n')
		return True

	else:
		raise ValueError

def ExitProg():
	exit()

def Clear():
	if name == 'nt':
		system('cls')

	else:
		system('clear')

def AskToPlay(Played):
	Menu = '''Guess Number Game

[1] Guess 1 - 10
[2] Guess 1 - 50
[3] Guess 1 - 100
[4] Guess 1 - 150
[5] GUess 1 - 200'''
	if Played == 0:
		print(Menu)
		UserMenu = input('\n[Type Q for Exit] Choose Menu: ').upper()

		if UserMenu == 'Q':
			ExitProg()

	else:
		UserMenu = input('\nPlay Again? [Y/N]: ').upper()
		Clear()

		if  UserMenu == 'Y':
			print(Menu)
			UserMenu = input('\n[Type Q for Exit] Choose Menu: ').upper()

			if UserMenu == 'Q':
				ExitProg()
				
			else:
				pass

		elif UserMenu == 'N':
			ExitProg()

		else:
			raise ValueError

	return UserMenu

def Probality(StoreProb, Prob, Played):
	StoreProb.append(Prob)
	
	if Played >= 1:
		print('Total Your Chance to get Correct Guess: ')
		for Num, Prob in enumerate(StoreProb):
			print(' {}. {}%'.format(Num+1,Prob))

	return StoreProb

StoreProb = []
Played = 0

Clear()
while True:
	try:
		Guessing = 1
		UserMenu = AskToPlay(Played)

		Clear()

		UserMenu = int(UserMenu)
		Number, RandRange = Menu(UserMenu)

		while True:
			try:
				print('\n[Type Q for Exit] Guess Number 1 - {}!'.format(RandRange))
				UserGuess = input('Your Guess: ').upper()

				if UserGuess == 'Q':
					ExitProg()
				
				else:
					Clear()
					UserGuess = CheckNumber(UserGuess, Number, RandRange)

					if UserGuess == True:
						Prob = ceil((1/Guessing) * 100)
						print('Your Chance to Get Correct Guess: {}%'.format(Prob))
						StoreProb = Probality(StoreProb, Prob, Played)
						Played += 1
						
						break

					else:
						Guessing += 1
						pass

			except ValueError:
				print('\nOops, Something Went Wrong.')

	except (ValueError, KeyError, KeyboardInterrupt):
		print('\nOops, Something Went Wrong.')