rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random as rm
pcdraw = rm.randint(1,3)
print("Hey Let's play Rock for 1 Paper for 2 and Scissors for 3")
ans = input('What you wanna draw Rock, paper, scissors.\n').lower()
print("Your Draw")
if(ans == "1"):
    print(rock)
    ans = 1
if (ans == "2"):
    print (paper)
    ans = 2
if (ans == "3"):
    print(scissors)
    ans = 3
print("Computer Draw:")
if(pcdraw == 1):
    print(rock)

if (pcdraw == 2):
    print (paper)
if (pcdraw == 3):
    print(scissors)

if (ans == pcdraw):
    print("It's Draw Start again")
if (ans ==1 and pcdraw== 2):
    print("PC win")
if (ans == 1 and pcdraw==3):
    print("You win")
if (ans ==2 and pcdraw == 1):
    print("You win")
if (ans ==2 and pcdraw == 3):
    print("Pc win")
if (ans==3 and pcdraw==1):
    print("Pc win")
if (ans==3 and pcdraw== 2):
    print("You Won")
