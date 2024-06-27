import art
from art import logo
print(logo)
print("Welcome To Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
import random
number=random.randint(1,100)

level=input("Choose a level of difficulty,Type hard for level hard and easy for level easy!")

def easy():
  print("you chose level easy, you get 10 guesses")
  flag=True
  while flag==True:
   for i in range(10):
     guess=int(input("guess a number"))
     if guess>number:
       print("too high")
       print(f"you have {9-i} guesses left")
     elif guess==number:
       print("correct guess,you win")
       flag=False
     elif guess<number:
       print("too low")
       print(f"you have {9-i} guesses left")
     else:
       print(f"you have {9-i} guesses left")
   print("you have no guesses left,you lose")
   print(f"The Number was {number}") 
   flag=False   

def hard():
  print("you chose level hard, you get 5 guesses")
  flag=True
  while flag==True:
   for i in range(5):
     guess=int(input("guess a number"))
     if guess>number:
       print("too high")
       print(f"you have {4-i} guesses left")
     elif guess==number:
       print("correct guess,you win")
       flag=False
     elif guess<number:
       print("too low")
       print(f"you have {4-i} guesses left")
     
   print("you have no guesses left,you lose") 
   print(f"The Number Was {number}") 
   flag=False  
    
if level=="easy":
  easy()
else:
  hard()