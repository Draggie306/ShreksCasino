import random, asyncio, time, base64, emoji, os, sys
global money # Currency Symbol: ඞ (Amogués)
import colorama
from colorama import Fore, Style
#import discord
#print("Me looking at your mother \U0001F346 \U0001F351	\U0001F4A7	")
def slowprint(s, egg: int):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./egg)
		
# Emoji List:
#https://unicode.org/emoji/charts/full-emoji-list.html

#https://venge.io/#81E6EC

# How to use the emojis:
#https://www.journaldev.com/52243/python-emoji-module#:~:text=Python%20Emoji%20Module%20%E2%80%93%20How%20to%20use%20emojis,Implementing%20Python%20Emoji%20module.%20...%204%20Conclusion.%20


#print(Style.BRIGHT + Fore.GREEN)
shrek = (" ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆\n ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿\n ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀\n ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀ \n ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉\n\n")

rock_eyebrow =("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⠋⠈⠀⠀⠀⠀⠐⠺⣖⢄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡏⢀⡆⠀⠀⠀⢋⣭⣽⡚⢮⣲⠆⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⡼⠀⠀⠀⠀⠈⠻⣅⣨⠇⠈⠀⠰⣀⣀⣀⡀⠀⢸⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢷⣶⠶⣃⢀⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠈⠓⠚⢸⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⡠⠀⡄⣀⠀⠀⠀⢻⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠐⠉⠀⠀⠙⠉⠀⠠⡶⣸⠁⠀⣠⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣦⡆⠀⠐⠒⠢⢤⣀⡰⠁⠇⠈⠘⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠠⣄⣉⣙⡉⠓⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")

shrek_or_rock = random.randint(1,100)# beans
if shrek_or_rock == 69:
  slowprint(Fore.GREEN + rock_eyebrow, 240)
else:
  slowprint(Fore.GREEN + shrek, 240)

def Blackjack():
  class player():
    cards = []
    card_total = int(0)
    def updateCards():
      for i in range(0, len(cards)):
        card_total += cards[i]
  
  class dealer():
    cards = []
    card_total = int(0)
    def updateCards():
      for i in range(0, len(cards)):
        card_total += cards[i]

  spades = {"1":("♠", 1), "2":("♠", 2), "3":("♠", 3), "4":("♠", 4), "4":("♠", 4), "5":("♠", 5), "6":("♠", 6), "7":("♠", 7), "8":("♠", 8), "9":("♠", 9), "10":("♠", 10), "J":("♠", 10), "Q":("♠", 10), "K":("♠", 10), "A":("♠", 11)}

  hearts = {"1":("♥", 1), "2":("♥", 2), "3":("♥", 3), "4":("♥", 4), "4":("♥", 4), "5":("♥", 5), "6":("♥", 6), "7":("♥", 7), "8":("♥", 8), "9":("♥", 9), "10":("♥", 10), "J":("♥", 10), "Q":("♥", 10), "K":("♥", 10), "A":("♥", 11)}

  diamonds = {"1":("♦", 1), "2":("♦", 2), "3":("♦", 3), "4":("♦", 4), "4":("♦", 4), "5":("♦", 5), "6":("♦", 6), "7":("♦", 7), "8":("♦", 8), "9":("♦", 9), "10":("♦", 10), "J":("♦", 10), "Q":("♦", 10), "K":("♦", 10), "A":("♦", 11)}

  clubs = {"1":("♣", 1), "2":("♣", 2), "3":("♣", 3), "4":("♣", 4), "4":("♣", 4), "5":("♣", 5), "6":("♣", 6), "7":("♣", 7), "8":("♣", 8), "9":("♣", 9), "10":("♣", 10), "J":("♣", 10), "Q":("♣", 10), "K":("♣", 10), "A":("♣", 11)}

  cards = [spades, hearts, diamonds, clubs]

  def draw(turn):
    if turn == "player":
      player.cards.append(random.choice(random.choice(cards)))
    elif turn == "dealer":
      dealer.cards.append(random.choice(random.choice(cards)))



  
#sort of works, doesnt crash but doesnt give output
def numpicker():
  global money
  bet = int(input("How much money do you want to bet? >"))
  if bet > money:
    print("😂😂😂 Get out you poor person!")
    quit()
  number = int(input("Pick a number from 1 to 30 >"))
  evens = ["2","4","6","8","10","12","14","16","18","20","22","24","26","28","30"]
  if number == evens:
    print("Well done! 2× bonus!")
    bet = bet * 2
    money = money + bet
    print(F"You now have ඞ{money}.")#	Class
  primes = ["1","2","3","5","7","11","13","17","19","23","29"]
  if number == primes:
    print("Well done! 5× bonus!")
    bet = bet * 5
    money = money + bet
    print("well done, 5x bonus!")
    print(F"You now have ඞ {money}.")

    
    if number == "10" or "20" or "30":
      bet = bet * 3
      money = money + bet
      print("good job, 3x bonus!")
      print(F"You now have ඞ {money}.")
    
    if number < 5:
      print("You get a 2× bonus, WOO HOO!")
      bet = bet * 2
      money = money + bet
      print(F"You now have ඞ {money}.")
		

# Roulette
def roulette():
    global money
    guess = int(input("What will the roulette spin be?(1-30) >"))
    colour = str(input("Red or black? >"))
    colour = colour.lower()
    roulette1 = random.randint(1,30)
    colour_list = ["red","black"]
    colour1 = random.choice(colour_list)
    if colour == colour1:
      print("You got the right colour! You won £100!")
      money = money + 100
      print(F"You now have ඞ {money}.")
    else:
      print("wrong colour")
    if guess == roulette1:
        print("BIG WIN! You won £1000!")
        money = money + 1000
        print(F"You now have ඞ {money}.")
        treble = input("Do you want a chance to treble it?>")
        if treble == "yes":
            guess2 = input("What will the roulette spin be? >")
            roulette2 = random.randint(1,30)
        if guess2 == roulette2:
            money = money * 3
            print(f"You now have ඞ {money}.")
        elif treble == "no":
          print("well youre boring")
    else:
        time.sleep(0.5)
        print("Wrong number. Bad luck, bozo!")





# Slot Machine - roll 3 and get dupes to win!
def find_3_in_row(slotmac_result):
  if slotmac_result[0] == slotmac_result[1]:
    pos0is1 = True
  else:
    pos0is1 =  False
  if slotmac_result[1] == slotmac_result[2]:
    pos1is2 = True
  else:
    pos1is2 = False
  if slotmac_result[0] == slotmac_result[2]:
    pos0is2 = True
  else:
    pos0is2 = False
  if pos0is1 == True and pos1is2 == True:
    in_a_row = 3
  elif pos0is1 == True or pos1is2 == True or pos0is2 == True:
    in_a_row = 2
  else:
    in_a_row = 1
  return in_a_row
def slotmac():
  global money
  slots = input("Pull the slot machine! It will cost ඞ 10.")
  if money < 10:
    print("You are too poor lololol get gud kid")
  else:
    money = money - 10
    print(f"You now have ඞ {money}.")
    slots = slots.lower()
    pull = ["\U0001F34B","\U0001F352","\U0001F34A","\U0001F680"]
    slotmac_result = []
    if slots == "yes" or slots == "y":
      for i in range(1,4):
        goodluck = random.choice(pull)
        slotmac_result.append(goodluck)
      print(slotmac_result)
      three_in_a_row = find_3_in_row(slotmac_result)
      if three_in_a_row == 3:
        print("3 IN A ROW! You win ඞ 200!")
        money = money + 200
        print(f"You now have ඞ {money}.")
      elif three_in_a_row == 2:
        print("2 in a row! You win ඞ 30!")
        money = money + 30
        print(f"You now have ඞ {money}.")
      else:
        print("You lose.")

# Intro and Credit Card System
print("Welcome to Shrek's Swamp Casino! \U0001F633")
print("\n\nHere, winning is so easy that it feels as dirty as my outhouse!\n\n")
global money

credit_card = (input("What is your credit card number?\n> "))

def call_credit_balance(cardNum):
	global money, credit_card

	credit_balance_file_directory = (f"cards/{cardNum}.txt")

	# If the balance file exists
	if os.path.isfile(f"{credit_balance_file_directory}"):
		with open (f"{credit_balance_file_directory}", "r") as f:
			money = f.read()
			#print(f"Money: {money} @15")
			f.close()

	# If not, open it and write 500 encoded
	else:
		with open (f"{credit_balance_file_directory}", "w") as f:
			money = 500
			f.write(f"{money}")
			f.close()
			#print(f"Money: written to 500 @24")

	x = open(credit_balance_file_directory, 'r')
	money = x.read()
	x.close()
			
	slowprint(f"You have ඞ {money} to play with. Have fun!\n", 30)

call_credit_balance(credit_card)

wrongspell = True
Games = ["Roulette","Numpicker","Slots","Blackjack","Higher or Lower","Ten Seconds"]

def wordle():
  import wordle


# Higher or Lower
def HoL():
  global money
  bet = input(f"You have ඞ {money}, how much do you want to bet?")
  game_num = random.randint(0, 100)
  choice = input(f"{game_num}/100\nHigher(H) or Lower(L)")
  if choice == "H" or choice == "h":
    if game_num < random.randint(0, 100):
      money = money + bet
    else:
      money = money - (bet * 2)
  elif choice == "L" or choice == "l":
    if game_num > random.randint(0, 100):
      money = money + bet
    else:
      money = money - (bet * 2)

# Ten Seconds - press enter after EXACTLY 10 sec to win!
def ten_seconds():
  global money
  ten_sec = input("Begin the countdown! It will cost ඞ 10.")
  if money < 10:
    print("You are too poor lololol get gud kid")
  else:
    money = money - 10
    print(f"You now have ඞ {money}.")
    time.sleep(0.5)
    print("The game will start in 3...")
    time.sleep(1)
    print("The game will start in 2...")
    time.sleep(1)
    print("The game will start in 1...")
    time.sleep(1)
    start=time.time()
    ten_sec_text = input("Begin! Press [ENTER] after 10 seconds!")
    end = time.time()
    duration = round(end - start,2)
    print(f"You pressed [ENTER] after {duration}.")
    if duration > 10.33:
      print("Too slow!")
    elif duration < 9.67:
      print("Too fast!")
    elif duration > 10 and duration < 10.33:
      dura_diff = duration - 10
      print(f"You were {dura_diff} seconds too slow.")
      ten_sec_reward = dura_diff * 10
      ten_sec_reward = ten_sec_reward.round(0)
      print(f"You win ඞ {ten_sec_reward}.")
    elif duration > 10 and duration < 10.33:
      dura_diff = 10 - duration
      print(f"You were {dura_diff} seconds too fast.")
      ten_sec_reward = dura_diff * 10
      ten_sec_reward = ten_sec_reward.round(0)
      print(f"You win ඞ {ten_sec_reward}.")
    elif duration == 10:
      print("You were bang on 10 seconds!")
      print("You win ඞ 100!")
      money = money + 100
      print(f"You now have {money}!")
      
# Game selection
while wrongspell == True:
  global money
  print("What game would you like to play?")
  print(*Games, sep=', ')
  print("Input \"money\" to display your balance.")
  choice = input(" > ")
  if choice == "money":
    print(f"You have ඞ {money}.")
  elif choice == "roulette":
    roulette()
    wrongspell = False
  elif choice == "numpicker":
    numpicker()
    wrongspell = False
  elif choice == "slots":
    slotmac()
    #wrongspell == False
  #elif choice == "higher or lower":
    #hoL()
    #wrongspell == False
  elif choice == "blackjack":
    Blackjack()
    wrongspell = False
  elif choice == "ten seconds":
    ten_seconds()
    wrongspell = False
  elif choice == "↑↑↓↓←→←→ba":
    konami_gen = random.randint(1,11)
    konami_gen_str = str(konami_gen)
    print(f"SECRET UNLOCKED! You gained {konami_gen_str} free amogués!")
    money = money + konami_gen
    print(f"You now have ඞ {money}.")
    





numpicker()
roulette()
hoL()
Blackjack()
slotmac()