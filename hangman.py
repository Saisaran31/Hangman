import random
chosen = list(random.choice(["kamal" , "rajini" , "vijay" , "ajith"]))
hidden = list("-" * len(chosen))
print("H A N G M A N")
count=0
while count < 8 and hidden!=chosen:
   print()
   print("".join(hidden))
   guess = input("enter the letter:")
   if len(guess) > 1:
       print("enter the single value:")
   if guess.isupper() == True:
       print("enter only lowercase value:")
   if guess in chosen:
       for i in range(len(chosen)):
           if chosen[i] == guess:
               hidden[i] = guess
if hidden == chosen:
    print("you found the word")
    print("good job")
else:
    print("you lost")




