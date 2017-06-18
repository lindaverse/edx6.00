
print("Please think of a number between 0 and 100!")
upper = 100
lower = 0
num = int((upper + lower) / 2)
ans = input("Is your secret number: " + str(num) + "? Enter 'h' to indicate the guess is too high. Enter 'l' to "
                                                   "indicate the guess is too low. Enter 'c' to indicate I guessed "
                                                   "correctly." ).lower()
while ans != "c":
    if ans == "h":
        upper = num
        num = int((upper + lower) / 2)
        ans = input("Is your secret number: " + str(num) + "? Enter 'h' to indicate the guess is too high. Enter "
                                                           "'l' to indicate the guess is too low. Enter 'c' to indicate "
                                                           "I guessed correctly.").lower()
    elif ans == "l":
        lower = num
        num = int((upper + lower) / 2)
        ans = input("Is your secret number: " + str(num) + "? Enter 'h' to indicate the guess is too high. Enter 'l' "
                                                           "to indicate the guess is too low. Enter 'c' to indicate I "
                                                           "guessed correctly.").lower()
    else:
        print("Sorry, I did not understand your input.")
        ans = input("Is your secret number: " + str(num) + "? Enter 'h' to indicate the guess is too high. Enter "
                                                           "'l' to indicate the guess is too low. Enter 'c' to indicate "
                                                           "I guessed correctly.").lower()
print("Game over. Your secret number was: " + str(num))

