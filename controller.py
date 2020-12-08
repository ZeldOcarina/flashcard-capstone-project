import pandas
import random


class Controller:
    def __init__(self):
        try:
            with open('data/words_to_learn.csv'):
                pass
        except FileNotFoundError:
            self.csv_data = pandas.read_csv('data/french_words.csv')
            self.raw_dictionary_data = self.csv_data.to_dict(orient="records")
            new_data = pandas.DataFrame(self.raw_dictionary_data)
            new_data.to_csv('data/words_to_learn.csv', index=False)
        else:
            self.to_learn_csv_data = pandas.read_csv('data/words_to_learn.csv')
            self.raw_dictionary_data = self.to_learn_csv_data.to_dict(orient="records")

    def choose_random_french_word(self):
        return random.choice(self.raw_dictionary_data)

    def cancel_data(self):
        new_data = pandas.DataFrame(self.raw_dictionary_data)
        new_data.to_csv('data/words_to_learn.csv', index=False)









