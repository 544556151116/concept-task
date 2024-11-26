import random
print("welcome to game_word")
word_list=["mostafa","ali","amgad","sayed"]
word=random.choice(word_list)
chosen_list=list(word)
random.shuffle(chosen_list)
script_word=''.join(chosen_list)
print(f"try the word:{script_word}")
x=5
print(f"you have {x} attempts.")
while x > 0:
    f=input("Enter your word: ")
    if( f == word):
        print("congratulations!")
        break
    else:
        x -=1
        if( x > 0) :
            print(f"incorrct word!you have {x}attempts left. ")
        else:
            print(f"you lost!the correct word is {word}")