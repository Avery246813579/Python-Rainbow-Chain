import random
import pickle

from Histogram import Histogram
from collections import deque
from FileParser import FileParser


class Dictogram:
    """ A Dictogram is a custom data type we use to store data for our Markov Chain. We use key (a word or phrase) then
    a histogram (of following words or phrases) to store our data.

    I refer to key and value a lot during this class. A key is the current word or phrase we are looking at (it can be
    a word of phrase because of the order we are using). A value is the word or phrase following our current key.
     """

    def __init__(self, words, order):
        """ Constructing the Dictogram

        :param words:       The words you want to add (the corpus)
        :param order:       The Markov Chain order
        """

        self.forwards = dict()
        self.backwards = dict()
        self.word_count = len(words)

        self.data = []
        self.sentence_starts = []
        self.sentence_ends = []

        self.construct_data(self.forwards, order, words, False)
        self.construct_data(self.backwards, order, list(reversed(words)), True)
        # self.construct_us(words, order)

    def construct_us(self, words, order):
        orders = []
        windows = []
        indexes = []

        reversed_words = list(reversed(words))

        # Go through all orders and construct their information
        for i in range(1, order + 1):
            orders.append([dict(), dict()])

            forward_window = deque(words[0: i])
            backward_window = deque(words[1: i + 1])

            windows.append([forward_window, backward_window])
            indexes.append(i)

        # Add first word to starting states
        self.sentence_starts.append(words[0])

        word_length = len(words)
        while len(words):
            indexes_length = len(indexes)

            for i in range(indexes_length):
                index = indexes[i]

                next_word = words[index]
                backward_word = words[index - order]
                order_windows = windows[i]

                if len(order_windows[0]) < i + 1:
                    order_windows[0].append(next_word)
                    order_windows[1].append(backward_word)
                    continue

                # If we are in first order and the next word is the end of a sentence list
                if next_word[-1] == '.':
                    next_word = next_word[:-1]

                    if i == 1:
                        # Add the next word to sentence ends
                        self.sentence_ends.append(next_word)

                        # If we are not at the end of our word list, add our word to start of sentence list
                        if index + 1 < word_length:
                            self.sentence_starts.append(words[index + 1])

                # Add for forward chain
                self.add(orders[i][0], tuple(order_windows[0]), next_word)
                self.add(orders[i][1], tuple(order_windows[1]), backward_word)

                if words[index][-1] == '.':
                    windows[i][0].append(next_word)
                    windows[i][0].popleft()
                    windows[i][1].append(next_word)
                    windows[i][1].popleft()

                    self.add(orders[i][0], tuple(order_windows[0]), '[SPLIT]')
                    self.add(orders[i][1], tuple(order_windows[1]), '[SPLIT]')

                    order_windows[0].clear()
                    order_windows[1].clear()
                    continue

                windows[i][0].append(next_word)
                windows[i][0].popleft()
                windows[i][1].append(next_word)
                windows[i][1].popleft()

            # Increment all indexes and if it hits the end we add it to our data
            for i in range(indexes_length):
                indexes[i] += 1

                if indexes[i] == word_length:
                    self.data.insert(0, orders[i])
                    del indexes[i]

            if 1 > indexes_length:
                break

    def construct_data(self, data, order, words, backward):
        creating = False

        words_length = len(words)
        window = deque(words[0: order])

        if backward and window[0][-1] == '.':
            window[0] = window[0][:-1]

        # Used to find the start of sentences
        if backward:
            self.sentence_ends.append(tuple(window))
        else:
            self.sentence_starts.append(tuple(window))

        # We loop through all our words and if it has occurred we add the following word to a histogram. If it has not
        # occurred we construct a new histogram
        for i in range(order, words_length):
            current_word = words[i]

            if len(window) < order:
                window.append(current_word)
                continue

            if creating:
                if backward:
                    self.sentence_ends.append(tuple(window))
                else:
                    self.sentence_starts.append(tuple(window))

                creating = False

            if self.next_item(data, backward, window, current_word):
                creating = True
                window.clear()

                if backward:
                    window.appendleft(current_word[:-1])

    def next_item(self, data, backward, window, word):
        split = False

        if word[-1] == '.':
            if backward:
                self.next_item(data, backward, window, '[SPLIT]')

                return True
            else:
                word = word[:-1]
                split = True

        # Add current data to our Dictogram
        self.add(data, tuple(window), word)

        # Add the next number in the sequence
        window.append(word)

        if backward:
            window.popleft()
        else:
            if window.popleft() == '[SPLIT]':
                data.append(tuple(window))

        # End of Word
        if split:
            self.next_item(data, backward, window, '[SPLIT]')

            return True

    def random_start(self, backwards=False):
        """ Finds a random start to our sentence using the end keys list.

        :return:        A key to use in order to construct the start of a sentence
        """
        if backwards:
            return self.sentence_ends[random.randint(0, len(self.sentence_ends) - 1)]
        else:
            return self.sentence_starts[random.randint(0, len(self.sentence_starts) - 1)]

    def add(self, data, key, value):
        """ Adds a key-value pair to the data set.

         :param key:        The word or phrase that we are currently looking at
         :param value:      The value is the word or phrase following the key
         """

        # If the word or phrase has not been said before, we create a new histogram for that word.
        if key not in data:
            data[key] = Histogram()

        # Update the word phrase in the keys histogram
        data[key].update_word(value)

    def random_forward_key(self):
        """ Gets a random word or phrase from our data set """
        keys = list(self.forwards.keys())

        return keys[random.randint(0, len(keys) - 1)]

    def random_backward_key(self):
        """ Gets a random word or phrase from our data set """
        keys = list(self.backwards.keys())

        return keys[random.randint(0, len(keys) - 1)]

    def __str__(self):
        to_return = ''

        for i in range(len(self.data)):
            to_return += str(i) + ' ORDER: \nForward:' + str(self.data[i][0]) + '\nBackward:' + str(self.data[i][0]) + '\n'

        return to_return

        # return str(self.forwards) + '\n' + str(self.backwards)

if __name__ == "__main__":
    # file_reader = FileParser('static/test_data.txt')

    # test_dict = Dictogram(file_reader.words, 3)
    # print(test_dict)
    # print(str(test_dict.sentence_starts))
    # print(str(test_dict.sentence_ends))

    # with open('data.pickle', 'wb') as handle:
    #     pickle.dump(test_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('data.pickle', 'rb') as handle:
        test_dict = pickle.load(handle)
        print(test_dict.random_forward_key())

    print("HI")

