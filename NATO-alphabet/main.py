
import pandas
raw_data = "nato_phonetic_alphabet.csv"
data = pandas.read_csv(raw_data).to_dict()
data_frame = pandas.DataFrame(data)

new_dict = {row.letter: row.code for (key, row) in data_frame.iterrows()}

is_on = True
while is_on:
    user_input = input("Please enter your word below:\n").upper()
    # for key in new_dict.keys():
    #     if user_input == key:
    #         print(new_dict[key])
    result_list = [new_dict[letter] for letter in user_input]
    print(result_list)
    ask = input("Would you like to continue?(Yes/No)\n").lower()
    if ask == "yes":
        pass
    else:
        is_on = False

