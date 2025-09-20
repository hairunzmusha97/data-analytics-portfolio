import random

print("Welcome to the Number guessing game!")
print("I'm thinking of a number between 1 to 100")

guesses = []
secret_number = random.randint(1,100)

attempt =0
level = str(input("Choose a level from Easy, Medium and Hard: "))
result = level.lower()
if (result == "easy"):
    max_attempts=10
elif result == "medium":
    max_attempts=5
elif result=="hard":
    max_attempts=3
else:
    print("Invalid choice! Defaultin to medium.")
    max_attempts=5


while attempt < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    guesses.append(guess)
    attempt+=1

    if(guess == secret_number):
        print(f"Correct you guessed the number in the {attempt} tries.")
        break
    elif guess < secret_number:
        print("Too Low! Try again.")
    else:
        print("Too high! Try again.")

if guess != secret_number:
    print(f"Sorry, you've used all the {max_attempts} attempts.The number was {secret_number}.")
    print("Your guesses were", guesses)