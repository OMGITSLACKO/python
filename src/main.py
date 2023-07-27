import random
 
rand = random.randint(1,10)
guess = "0"

while int(guess) != rand:
  guess = input("What's your guess?")
  if guess == "q":
    print("YOU GAVE UP :( ")
    break
  elif int(guess) == rand:
    print ("YOU WIN!!!")
    break
  else:
    print("nope")
  