import random

class Histogram:
    """ Histogram is a class to store types and tokens

     We store all our data in a dictionary. Our key is the current word or phrase, and the value is the number of
     occurrences for that word.
     """

    def __init__(self):
        """ Initialize the data """
        self.data = {}
        self.word_count = 0

    def __len__(self):
        """ Gets the amount of words in the data set. Not types! """
        return self.word_count

    def update_word(self, word):
        self.word_count += 1

        if word in self.data:
            self.data[word] += 1
        else:
            self.data[word] = 1

    def random_word(self):
        random_range = random.random()
        total_word_count = len(self.data)
        last_percent = 0

        for current_word in self.data:
            word_occurrences = self.data[current_word]

            last_percent = frequency = last_percent + word_occurrences / total_word_count

            if random_range < frequency:
                return current_word

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return '[Histogram: ' + str(self.data) + "]"


if __name__ == "__main__":
    data = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

    gram = Histogram()
    for word in data:
        gram.update_word(word)

    dd = {}

    for i in range(10000):
        letter = gram.random_word()

        if letter in dd:
            dd[letter] += 1
        else:
            dd[letter] = 1

    print(dd)
