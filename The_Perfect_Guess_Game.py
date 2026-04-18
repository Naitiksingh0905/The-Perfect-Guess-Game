import random
n = random.randint(1, 101)
a = -1
print("Welcome to The Perfect Guess Game!\nGuess any number from 1 to 100.")
guesses = 1
while(a!=n):
    a = int(input("Enter your guess:"))
    if (a > n):
        print("Lower number please.")
        guesses+=1
    elif(a<n):
        print("Higher number please.")
        guesses +=1
print(f"You guessed the number {n} correctly in {guesses} attempts.")
    