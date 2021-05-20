import pandas

nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {
    row.letter: row.code
    for (_, row) in nato_alphabet_df.iterrows()
}

user_input = input("Enter a word: ").upper()

code = [nato_dict[letter] for letter in user_input if nato_dict.get(letter)]
print(code)
