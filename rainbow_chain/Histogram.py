import random


class HistogramWithCount:
    """ Histogram is a class to store types and tokens

     We store all our data in an array of arrays. The internal arrays we will be calling nodes. Each node represents
     a respected number of word occurrences. The node has three values at the indexes 0, 1.

     0: The number of occurrences
     1: A list of words that occur (0) amount of times
     """

    def __init__(self):
        """ Initialize the data """
        self.nodes = []
        self.word_count = 0

    def __len__(self):
        """ Gets the amount of words in the data set. Not types! """
        return self.word_count

    def __str__(self):
        """ THe string representation of the nodes """
        return str(self.nodes)

    def update_word(self, word):
        """ If the word is already in the histogram we will update the number of times the word occurs. If not then
        we insert it into our nodes

        :param word:     The word we want update in the data set
        """

        self.word_count += 1
        length = len(self.nodes)

        # If we have no data. Let's just create a new node.
        if length < 1:
            self.nodes.append([1, [word]])
            return

        for i in range(length):
            current_node = self.nodes[i]
            words = current_node[1]

            # If our word is in the current node. Remove it then check more things.
            if word in words:
                words.remove(word)

                # If there are no following nodes. We are the greatest node and can just add a new node
                if i > length - 2:
                    self.nodes.append([current_node[0] + 1, [word]])
                else:
                    next_node = self.nodes[i + 1]

                    # If the next nodes occurrences is equal to one more then the current node. We add our word to the
                    # next node. If not, then we create a new node there.
                    if next_node[0] == current_node[0] + 1:
                        next_node[1].append(word)
                    else:
                        self.nodes.insert(i + 1, [current_node[0] + 1, [word]])

                # If there are no words left in this node. We delete the node.
                if len(words) < 1:
                    del self.nodes[i]

                return

        # We check if the first nodes occurrences is 1. If it is we add our word. If not, we create a new node that
        # the occurrences is one
        if self.nodes[0][0] == 1:
            self.nodes[0][1].append(word)
        else:
            self.nodes.insert(0, [1, [word]])

    def random_word(self):
        """ Gets a random word from the histogram

        :return:    The random word
        """

        number = random.random()
        word_count = self.word_count
        last_percent = 0
        for node in self.nodes:
            last_percent = frequency = last_percent + node[0] * len(node[1]) / word_count

            # If the number is greater then the percentage we calculated before, then this is the random node we want.
            # Then we get a random word from the node's second index which is the list of words
            if number < frequency:
                return node[1][random.randint(0, len(node[1]) - 1)]


class Histogram:
    """ Histogram is a class to store types and tokens

     We store all our data in a dictionary. Our key is the current word or phrase, and the value is the number of
     occurrences for that word.
     """

    def __init__(self):
        """ Initialize the data """
        self.nodes = {}
        self.word_count = 0

    def __len__(self):
        """ Gets the amount of words in the data set. Not types! """
        return self.word_count

    def __str__(self):
        """ THe string representation of the nodes """
        return str(self.nodes)

    def update_word(self, current_word):
        """ If the word is already in the histogram we will update the number of times the word occurs. If not then
        we insert it into our nodes

        :param current_word:     The word we want update in the data set
        """

        self.word_count += 1

        if current_word in self.nodes:
            self.nodes[current_word] += 1
        else:
            self.nodes[current_word] = 1

    def random_word(self):
        """ Gets a random word from the histogram

        :return:    The random word
        """

        random_range = random.random()
        total_word_count = self.word_count
        last_percent = 0

        # Go through all our words checking if the one is coming up
        for current_word in self.nodes:
            word_occurrences = self.nodes[current_word]

            # We get the frequency of the word
            last_percent = frequency = last_percent + word_occurrences / total_word_count

            # If the number is greater then the percentage we calculated before, then this is the random node we want.
            if random_range < frequency:
                return current_word

    def __repr__(self):
        return "Histogram[" + str(self.nodes) + "]"


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
