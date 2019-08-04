import time
import random
def print_pause(text_to_print):
   print(text_to_print)
   time.sleep(1)
Attackers = ["The wicked fairie", "The grogon",
            "the Dragon", "the Monsters", "snake"]
test = random.choice(Attackers)
def start():
   print_pause("You are too late for your business in the company")
   print_pause("You want to get to your company quickly")
   print_pause("while you were walking in a dark street,"
               "You found two different ways")
   print_pause(f"and the {test} attacks you! \n")
   reaction()
def reaction():
   while True:
       Act = input("Enter '1' to turn right\n"
                   "Enter '2' to turn left :")
       if Act == "1":
           print_pause("Excellent.You entered the right\n"
                       "way . You arrived to your company"
                       "as fast as possible")
           play_again()
       elif Act == "2":
           print_pause("Wrong choice")
           play_again()
           break
   else:
       return Act
# noinspection PyInterpreter
def play_again():
   while True:
       Act = input("Play again?\n"
                   "Enter 'yes' or 'no' .\n")
       if Act == "yes":
           start()
           reaction()
           play_again()
       if Act == "no":
           print_pause("Wish you the best of luck")
           exit()
   else:
       return Act
start()
reaction()
play_again()