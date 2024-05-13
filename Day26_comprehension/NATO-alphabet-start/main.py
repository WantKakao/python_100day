#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {val.letter:val.code for (idx, val) in dataframe.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
new_list = [new_dict[letter] for letter in user_input]
print(new_list)
