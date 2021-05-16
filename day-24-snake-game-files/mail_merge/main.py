names = []
# reading Names
with open("Input/Names/invited_names.txt", mode="r") as names_file:
    for name in names_file.readlines():
        names.append(name.strip())

starting_letter = ''
# reading starting letter
with open("Input/Letters/starting_letter.txt", mode="r") as start:
    starting_letter = start.read()

# writing personalized letters
for name in names:
    letter = starting_letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt",
              mode="w") as letter_file:
        letter_file.write(letter.strip())
