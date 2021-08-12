import random
words=[]
a=input("enter your name : ")
with open('name.txt','r') as file:
    for line in file:
        for word in line.split():
            words.append(word)
word = random.choice(words)
print("Find the name")
temp = ''
chances = 4
while chances > 0:
    lost = 0
    for char in word:
        if char in temp:
            print(char,end=" ")
        else:
            print("-",end=" ")
            lost += 1
    if lost == 0:
        print("\nCongratilations You have won",a)
        print("The word is: ", word)
        break
    guess = input("\nEnter the letter:")
    temp += guess
    if guess not in word:
        chances = chances- 1
        print("You have", + chances, 'more guesses')
        if chances == 0:
            print("\nYou have Lost ",a)
            print("The name is",word)
