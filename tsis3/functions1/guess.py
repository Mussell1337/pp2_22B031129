name = str(input("Hello, What is your name?: "))
print("Well, {}, I am thinking of a number between 1 and 20".format(name))
guess = 0
stop_print = False
while True:
    guess += 1
    num = int(input())
    if num == 19:
        print("Good job, {}! You guessed my number in {} guesses!".format(name,guess))
        break
    elif num < 19:
        print("Your guess is too low")
    elif num > 19 and num <= 20:
        print("Your guess is too high")
    else:
        print("Out of range")