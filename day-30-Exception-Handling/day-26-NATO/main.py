import pandas

nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {
    row.letter: row.code
    for (_, row) in nato_alphabet_df.iterrows()
}

def generate_phonetics():
    user_input = input("Enter a word: ").upper()
    try:
        code = [nato_dict[letter] for letter in user_input if nato_dict[letter]]
    except KeyError:
        print("Please enter only letters!")
        generate_phonetics()
    else:
        print(code)


generate_phonetics()
