#Lottery exercise
#Learnt: and, or

win = input("Have you win at the lottery?")
if win == 'y':
    winner = True
    winAmountString = input("How much money have you won?")
    winAmount = int(winAmountString)
    if winner and winAmount > 1000000 :
        print("Whoa! You can retire! :)")

areYouRich = input("Are you a damn rich dude?")
if win == 'y' or areYouRich == 'y':
        print("Whoa! You can retire! :)")
