import random



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',  '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 4
end = False
list =[ "nithin", "energy","disgusting", "rahul"]
word = random.choice(list)


print(" welcome to guess game ")

dis = []
for i in range(len(word)):
    dis+= "_"
print(dis)
while not end:
    guess = input(" guess a letter       ").lower()
    if guess in dis:
        print(f"You've already guessed {guess}")


    for position in range(len(word)) :
        letter = word[position]
        if letter == guess:
            dis[position] = letter

    if guess not in word:
            lives -= 1
            if lives == 0:
                end = True
                print("You lose.")
                print(f"the answer is {word}")
    print(f" {''.join(dis)}")               
    if "_" not in dis:
        end_of_game = True
        print("You win.")
    print(stages[lives])


