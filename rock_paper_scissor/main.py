import random

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
images = [ rock , paper, scissors]

i = 0
while (i ==0):
    choice = int(input(" what you choose ?, 0 for rock, 1 for papper, 2 for  scissors \n"))
    if choice >=3 or choice <0:
        print(" you have enterd an invalid number")
    else:
        print(" you choose ")
        print(images[choice])
        cmp_choice = random.randint(0,2)
        print("computer choose")
        print(images[cmp_choice])

        if choice == 0 and cmp_choice == 2:
            print(" you win!")
        elif  cmp_choice == 0 and choice==2:
            print(" you loose !! ")
        elif cmp_choice > choice:
            print("you loose !")
        elif cmp_choice< choice:
            print(" you win!")
        
    i = int(input(" enter 0 if u want too play again or 1 to quit\n"))
    