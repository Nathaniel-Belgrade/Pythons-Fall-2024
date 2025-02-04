#This program is a scrabble score calculator.
#When ran, the program will ask for an input. You can put in any combination of letters.
#After taking in your inputted "word", 
#it will check each letter of the word, and find it's corresponding value within the dictionary
#Finally, it will print the value to your inputted "word"

#Alphabet storing all possible letters to a certain value
alphabet = {
    'aeilnorstu':1,
    'dg':2,
    'bcmp':3,
    'fhvwy':4,
    'k':5,
    'jx':8,
    'qz':10,
    '1234567890':0
}
#grabs inputted word, sets it to lowercase to match alphabet
word = input("Input a word: ").lower()
total = 0

#for loop for all letters in word
for letter in word:
#for loop for all alphabet keys
    for key, value in alphabet.items():
#if current letter in word is in the key, add the value of the letter to the total.
        if letter in key:
            total += value

print(f"The word {word.upper()} is worth {total} points in scrabble.")
