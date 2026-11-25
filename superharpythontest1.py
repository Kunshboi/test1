
secret = 27
max_attempts = 5
count = 0
guess = int(input("Enter your guess (between 1 and 50): "))
play = True 

print("=" * 42)
print(" 🎮 NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print("You have 5 attempts to guess the secret number.")
print()

if max_attempts > 0:
    print("You are safe")

elif max_attempts == 0:
    print("Game over")

else:
    print("You have" ,count, "attempts left")

if count == max_attempts:
    print("Game over You've used all your attempts.")

else :
    print("You have" ,count, "attempts left")

if guess == secret:
    print("Well done your correct")

elif guess > 10 :
    print("The number is odd")

elif guess > 20 :
    print("The number is not a prime number")

elif guess > 30 :
    print("if a=27 b=3 then what factor do they have multiply it by 3 to get the number")

elif guess > 40 :
    print("The number is divisible by not divisible by 2")

elif guess > 50 :
    print("Too high")

if guess > secret:
    guess = int(input("Try again  "))

elif guess < secret:
    guess = int(input("Try again "))

else:
    print("wow")

if guess is not secret:
    stop = input("Wanna stop playing yes or no? ")
else:
    print("You guessed the secret number! Congratulations!")

if stop == "yes":
    print("Game over")

else:
    guess = int(input("Try again "))

if play == True:
    guess = int(input("Go On "))

else:
    print("wow")

if guess == secret:
    print("you win")

else: 
    print("times up")



    
    
