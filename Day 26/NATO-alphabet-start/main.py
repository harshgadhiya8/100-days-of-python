
import pandas as pd

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for(index,row) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input('Enter the word ').upper()
    try:
        output_word =[nato_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, Only letters in the alphabet: ')
        generate_phonetic()
    else:
        print(output_word)

generate_phonetic()

