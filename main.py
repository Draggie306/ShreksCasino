version_number = "v0.1"

import random, asyncio, time, base64, os, sys, emoji, colorama, webbrowser, itertools
global money, credit_card  # Currency Symbol: ඞ (Amogués)

from colorama import Fore, Style


#import discord
#print("Me looking at your mother \U0001F346 \U0001F351	\U0001F4A7	")
def slowprint(s, egg: int):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / egg)

def slowprintlist(s: list, egg: int):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / egg)            

x = True
while x == True:
  objects_ive_shoved = ["small glass jars", "broomstick handles", "balls", "fingers", "Brite Bomber","ur mom","Ismail","Jacob Eke-Cunis", "Joe and Charlie Sewards", "men", "women", "young boys", "Benjamin Ford", "Will Byrne", "Fortnite books", "ben ps", "Discord Nitro", "Harry Barwick", "Vytautus", "Amogus", "beans", "hydrocarbons", "Samuel Partrige", "Mrs Arnold (it was disgusting)", "Sam Fisher", "Jack Fisher", "Jess Fisher", "Chloë Fisher", "adolfus", "joesphy spaghetti", "tigger_4", "emilite shards"]
  print(f"\"Today, I have used {random.choice(objects_ive_shoved)},\" said Shrek.")
  x = False
def dev_tools():  #	Call this when you want details for debugging
    print(
        f"\n--------- DevTools subroutine --------- \nMoney (variable) = {money}"
    )
    call_credit_balance_first(credit_card)
    print(f"Money from file = {money}")
    print(f"Credit card number = {credit_card}")
    path, dirs, files = next(os.walk("cards/"))
    cards = len(files)
    print(f"Money accounts = {cards}")
    print(f"--------- End of DevTools --------- \n\n")


def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


# Emoji List:
#https://unicode.org/emoji/charts/full-emoji-list.html

#https://venge.io/#81E6EC

# How to use the emojis:
#https://www.journaldev.com/52243/python-emoji-module#:~:text=Python%20Emoji%20Module%20%E2%80%93%20How%20to%20use%20emojis,Implementing%20Python%20Emoji%20module.%20...%204%20Conclusion.%20

#webbrowser.open("https://soap2day.ac/MczozMToiOTE2fHwxMzguNjguMTUyLjE5Nnx8MTY0NjM4OTYMil7.html << copy paste(use with vpn and dont use on school wifi :)")

#print(Style.BRIGHT + Fore.GREEN)
shrek = (
    " ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆\n ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿\n ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀\n ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀ \n ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉\n\n"
)

rock_eyebrow = (
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⠋⠈⠀⠀⠀⠀⠐⠺⣖⢄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡏⢀⡆⠀⠀⠀⢋⣭⣽⡚⢮⣲⠆⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⡼⠀⠀⠀⠀⠈⠻⣅⣨⠇⠈⠀⠰⣀⣀⣀⡀⠀⢸⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢷⣶⠶⣃⢀⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠈⠓⠚⢸⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⡠⠀⡄⣀⠀⠀⠀⢻⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠐⠉⠀⠀⠙⠉⠀⠠⡶⣸⠁⠀⣠⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣦⡆⠀⠐⠒⠢⢤⣀⡰⠁⠇⠈⠘⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠠⣄⣉⣙⡉⠓⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
)

# Intro and Credit Card System
shrek_or_rock = random.randint(1, 100)
if shrek_or_rock == 69:
    slowprint(Fore.GREEN + rock_eyebrow, 240)
else:
    #slowprint(Fore.GREEN + shrek, 240)
    print(Fore.GREEN + shrek)

print("Welcome to Shrek's Swamp Casino! \U0001F633")
print("Here, winning is so easy that it feels as dirty as my outhouse!\n")
global money, credit_balance_file_directory

try:
    credit_card = input("What is your credit card number?\n\n>>> ")
    credit_card = int(credit_card)
    dev_mode = False
    if credit_card == 6969:
        dev_mode = True
        dev = "Draggie"
    if dev_mode == True:
        if dev == "Draggie":
            print(Fore.BLUE + f"\n\nDeveloper mode enabled - {dev}")
except:
    print("It's called a credit card NUMBER \U0001F644\n")
    sys.exit()

def call_credit_balance(credit_card):
    global money, credit_balance_file_directory

    credit_balance_file_directory = (f"cards/{credit_card}.txt")

    with open(f"{credit_balance_file_directory}", "r") as f:
        money = f.read()
        f.close()

    money = int(money)
    print(f"You now have {money}.")

    #slowprint(f"You have ඞ {money} to play with. Have fun!\n", 30)
    # Change to int


def call_credit_balance_first(cardNum):
    global money, credit_card, credit_balance_file_directory

    credit_balance_file_directory = (f"cards/{cardNum}.txt")

    # If the balance file exists
    if os.path.isfile(f"{credit_balance_file_directory}"):
        with open(f"{credit_balance_file_directory}", "r") as f:
            money = f.read()
            f.close()

    # If not, open it and write 500 encoded
    else:
        with open(f"{credit_balance_file_directory}", "w") as f:
            money = 500
            f.write(str(money))
            f.close()
            #print(f"Money: written to 500")

    # To prevent weird errors, read money back from the file.
    x = open(credit_balance_file_directory, 'r')
    money = x.read()
    x.close()

    money = int(money)

    if money <= 0:
        print(
            "You're bankrupt. Please apply for a loan with a new credit card in order to play.\n\n\n\n\n\n\n"
        )
        sys.exit()
    #slowprint(f"You have ඞ {money} to play with. Have fun!\n", 30)
    # Change to int


def cool_bank_contacting():
    spinner = itertools.cycle('\\|/-')
    spinCount = 0
    while spinCount < (random.randint(10, 40)):
        sys.stdout.write(
            f"Contacting bank... {next(spinner)}")  # write the next character
        sys.stdout.flush()  # flush stdout buffer (actual character display)
        sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b'
                         )  # erase the last written char
        time.sleep(0.1)
        spinCount = spinCount + 1
    sys.stdout.write(
        f"Contacting bank... Done! The ping to the bank is {spinCount / 10} seconds."
    )


def change_credit_card_balance(toAdd):
    # Read current balance from global credit card file
    x = open(credit_balance_file_directory, 'r')
    current_balance = x.read()
    x.close()

    # Add the new balance to the parameter "toAdd"
    new_balance = int(current_balance) + int(toAdd)
    new_balance = (str(new_balance))

    # Clears the file to make it read zero
    x = open(credit_balance_file_directory, 'w+')
    x.close()

    # Finally, write the calculated amount to the file
    x = open(credit_balance_file_directory, 'w')
    x.write(new_balance)
    x.close()


call_credit_balance_first(credit_card)

try:
    if dev_mode == True:
        print(
            f"\nSuccessfully contacted your bank. Your card's balance is ඞ {money}."
        )
except:
    cool_bank_contacting()
    slowprint(
        f"\nSuccessfully contacted your bank. Your card's balance is ඞ {money}.",
        240)


# Game selection
def game_selection():
    global money
    wrongspell = True
    Games = [
        "Roulette", "Numpicker", "Slots", "Blackjack", "Higher or Lower",
        "Ten Seconds", "shrek1", "shrek2", "shrek musical", "money to 0"
    ]
    while wrongspell == True:
        slowprint("\nWhat game would you like to play?\n", 50)
        if dev_mode == True:
            dev_tools()
        print(*Games, sep=', ')
        print("You can also input \"money\" to display your balance.\n")
        choice = input(">>> ")
        choice = choice.lower()
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
        elif choice == "shrek1":
            print(
                "https://soap2day.ac/MczozMToiOTE2fHwxMzguNjguMTUyLjE5Nnx8MTY0NjQxMzcwMyI7.html << copy paste(use with vpn and dont use on school wifi :)"
            )
        elif choice == "shrek2":
            print(
                "https://soap2day.ac/MczozMToiOTA4fHwxMzguNjguMTUyLjE5Nnx8MTY0NjQxMzc1NCI7.html"
            )
        elif choice == "shrek musical":
            print(
                "https://soap2day.ac/MczozMjoiOTcyNHx8MTM4LjY4LjE1Mi4xOTZ8fDE2NDY0MTM4NTAiOw.html"
            )
        elif choice == "↑↑↓↓←→←→ba" or choice == "^^vv<><>ba":
            konami_gen = random.randint(1, 11)
            konami_gen_str = str(konami_gen)
            print(
                f"SECRET UNLOCKED! You gained {konami_gen_str} free amogués!")
            money = money + konami_gen
            print(f"You now have ඞ {money}.")
        elif choice == "dev":
            raise SystemExit(
                f'{slowprint("Deez FAT balls are in your mouth right now!", 10)}'
            )
        elif choice == "shreks":
          x = open ("shrek1_transcript.txt", 'r')
          shrek_script = x.read()
          x.close()
          slowprint(shrek_script, 120)
        elif choice == "money to 0":
          money = 0
          #grei


# Blackjack (idk if it works)
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

    spades = {
        "1": ("♠", 1),
        "2": ("♠", 2),
        "3": ("♠", 3),
        "4": ("♠", 4),
        "4": ("♠", 4),
        "5": ("♠", 5),
        "6": ("♠", 6),
        "7": ("♠", 7),
        "8": ("♠", 8),
        "9": ("♠", 9),
        "10": ("♠", 10),
        "J": ("♠", 10),
        "Q": ("♠", 10),
        "K": ("♠", 10),
        "A": ("♠", 11)
    }

    hearts = {
        "1": ("♥", 1),
        "2": ("♥", 2),
        "3": ("♥", 3),
        "4": ("♥", 4),
        "4": ("♥", 4),
        "5": ("♥", 5),
        "6": ("♥", 6),
        "7": ("♥", 7),
        "8": ("♥", 8),
        "9": ("♥", 9),
        "10": ("♥", 10),
        "J": ("♥", 10),
        "Q": ("♥", 10),
        "K": ("♥", 10),
        "A": ("♥", 11)
    }

    diamonds = {
        "1": ("♦", 1),
        "2": ("♦", 2),
        "3": ("♦", 3),
        "4": ("♦", 4),
        "4": ("♦", 4),
        "5": ("♦", 5),
        "6": ("♦", 6),
        "7": ("♦", 7),
        "8": ("♦", 8),
        "9": ("♦", 9),
        "10": ("♦", 10),
        "J": ("♦", 10),
        "Q": ("♦", 10),
        "K": ("♦", 10),
        "A": ("♦", 11)
    }

    clubs = {
        "1": ("♣", 1),
        "2": ("♣", 2),
        "3": ("♣", 3),
        "4": ("♣", 4),
        "4": ("♣", 4),
        "5": ("♣", 5),
        "6": ("♣", 6),
        "7": ("♣", 7),
        "8": ("♣", 8),
        "9": ("♣", 9),
        "10": ("♣", 10),
        "J": ("♣", 10),
        "Q": ("♣", 10),
        "K": ("♣", 10),
        "A": ("♣", 11)
    }

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
    evens = [
        "2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "22", "24",
        "26", "28", "30"
    ]
    if number in evens:
        print("Well done! 2× bonus!")
        bet = bet * 2
        money = money + bet
        change_credit_card_balance(money)
        call_credit_balance(credit_card)  #	Class
    primes = ["1", "2", "3", "5", "7", "11", "13", "17", "19", "23", "29"]
    if number == primes:
        print("Well done! 5× bonus!")
        bet = bet * 5
        money = money + bet
        change_credit_card_balance(money)
        print("well done, 5x bonus!")
        call_credit_balance(credit_card)

        if number == "10" or "20" or "30":
            bet = bet * 3
            money = money + bet
            change_credit_card_balance(money)
            print("good job, 3x bonus!")
            call_credit_balance(credit_card)

        if number < 5:
            print("You get a 2× bonus, WOO HOO!")
            bet = bet * 2
            money = money + bet
            change_credit_card_balance(money)
            call_credit_balance(credit_card)

    game_selection()


# Roulette
def roulette():
    global money
    guess = int(input("What will the roulette spin be?(1-30) >"))
    colour = str(input("Red or black? >"))
    colour = colour.lower()
    roulette1 = random.randint(1, 30)
    colour_list = ["red", "black"]
    colour1 = random.choice(colour_list)
    if colour == colour1:
        print("You got the right colour! You won ඞ 100!")
        money = money + 100
        change_credit_card_balance(money)
        call_credit_balance(credit_card)
    else:
        print("wrong colour")
    if guess == roulette1:
        print("BIG WIN! You won £1000!")
        money = money + 1000
        change_credit_card_balance(1000)
        call_credit_balance(credit_card)
        treble = input("Do you want a chance to treble it?>")
        if treble == "yes":
            guess2 = input("What will the roulette spin be? >")
            roulette2 = random.randint(1, 30)
        if guess2 == roulette2:
            money = money * 3
            change_credit_card_balance(money)
            call_credit_balance(credit_card)
        elif treble == "no":
            print("well youre boring")
    else:
        time.sleep(0.5)
        print(f"Wrong number ({roulette1}). Bad luck, bozo!")
    game_selection()


# Slot Machine - roll 3 and get dupes to win!
def find_3_in_row(slotmac_result):
    if slotmac_result[0] == slotmac_result[1]:
        pos0is1 = True
    else:
        pos0is1 = False
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


# Slot Machine - continued
def slotmac():
    global money
    if money < 10:
        print("You are too poor lololol get gud kid")
    else:
        print("Pulling the slot machine... You have been charged ඞ 10.")
        money = money - 10
        change_credit_card_balance(-10)
        call_credit_balance(credit_card)
        pull = ["\U0001F34B", "\U0001F352", "\U0001F34A", "\U0001F346"]
        slotmac_result = []
        for i in range(1, 4):
            goodluck = random.choice(pull)
            slotmac_result.append(f"{goodluck} ")
        slowprintlist(slotmac_result, 1)
        three_in_a_row = find_3_in_row(slotmac_result)
        if three_in_a_row == 3:
            print("\n3 IN A ROW! You win ඞ 200!")
            money = money + 200
            change_credit_card_balance(200)
            call_credit_balance(credit_card)
        elif three_in_a_row == 2:
            print("\n2 in a row! You win ඞ 30!")
            money = money + 30
            change_credit_card_balance(30)
        else:
            print("You lost ඞ 10.")
    game_selection()


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
    #money = int(money)
    game_selection()


# Ten Seconds - press enter after EXACTLY 10 sec to win!
def ten_seconds():
    global money
    print("Begin the countdown! It will cost ඞ 10.")
    time.sleep(0.5)
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
        start = time.time()
        ten_sec_text = input("Begin! Press [ENTER] in 10 seconds!")
        end = time.time()
        duration = round(end - start, 2)
        print(f"You pressed [ENTER] after {duration} seconds.")
        if duration > 10.33:
            print("Too slow!")
            call_credit_balance(credit_card)
        elif duration < 9.67:
            print("Too fast!")
            call_credit_balance(credit_card)
        elif duration > 10 and duration < 10.33:
            dura_diff = duration - 10
            dura_diff = round(dura_diff, 2)
            print(f"You were {dura_diff} seconds too slow.")
            ten_sec_reward = dura_diff * 10
            ten_sec_reward = ten_sec_reward.round(0)
            change_credit_card_balance(ten_sec_reward)
            call_credit_balance(credit_card)
        elif duration > 10 and duration < 10.33:
            dura_diff = 10 - duration
            dura_diff = round(dura_diff, 2)
            print(f"You were {dura_diff} seconds too fast.")
            ten_sec_reward = dura_diff * 10
            ten_sec_reward = round(ten_sec_reward, 0)
            print(f"You win ඞ {ten_sec_reward}.")
            change_credit_card_balance(ten_sec_reward)
            call_credit_balance(credit_card)
        elif duration == 10:
            print("You were bang on 10 seconds!")
            print("You win ඞ 250!")
            money = money + 250
            change_credit_card_balance(250)
            call_credit_balance(credit_card)
    game_selection()


game_selection()

#numpicker()
#roulette()
#hoL()
#Blackjack()
#slotmac()
#ten_seconds()
