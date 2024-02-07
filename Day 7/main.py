import random
import hangman_art
import word
print(hangman_art.logo)
words = ["ardwark","baboon","camel","lion"]
chosen_word = word.word_list[random.randint(0,3)]
print(f"Word is {len(chosen_word)} letters long")
lives = 6
guessed_word = []
g_w = ""
for i in chosen_word: guessed_word.append('_')
while lives>0 and chosen_word != g_w:
    l = input("Enter a letter: ").lower()
    if l in chosen_word:
        for position in range(len(chosen_word)): 
            if l == chosen_word[position]:
                guessed_word[position] = l
        print(hangman_art.stages[lives])
    else:
        print("You lost a life")
        lives -=1
        print(hangman_art.stages[lives])
        
    g_w = ''.join([str(elem) for elem in guessed_word])
    print(g_w)

if g_w == chosen_word:
   print("You won")
else:
   print("You lose")
   print(f"The word was {chosen_word}")