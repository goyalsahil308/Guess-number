import random

a=random.randint(1,200)
print(a)
guess=0
b=None
while (b!=a):
   guess=guess+1
   b=int(input("Guess the number: "))
   if guess!=10:
    if (a>int(b)):
      print("Higher number please:")
    elif(a<int(b)):
      print("Lower number please: ")
    elif(a==int(b)):
      print("Congrats you have guessed thr right number")
      print(f"Guessed in {guess} guessess")
      break
   else:
      print(f"Enough guesses .The right number is {a}.Good luck next time")
      break
with open("highscore111.txt","r") as f:
   f1=f.read()
if (f1=="" or int(f1)>guess):
    with open("highscore111.txt","w") as f:
        f.write(str(guess))
       