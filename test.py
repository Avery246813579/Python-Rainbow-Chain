import random

words = 'And if you look closely, you can see a 16-year old boy, looking right at the camera, right into your eyes. You can see Elie. Dogs taste good dog. Can I read a book today? Yeah I love to eat. It is good. Very good thing mom. Teehe xd'.split()


class Histogram:
    def __init__(self):
        self.data = {}

    def update_word(self, word):
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


# class Dictogram:
#     def __init__(self, words):
#         self.data = {}
#
#         for i in range(len(words) - 1):
#             state = words[i]
#             next_word = words[i + 1]
#
#             if state[-1] == '.':
#                 self.add(state[:-1], '[SPLIT]')
#                 self.add('[SPLIT]', next_word)
#                 continue
#
#             if next_word[-1] == '.':
#                 next_word = next_word[:-1]
#
#             self.add_to_dictogram(state, next_word)
#
#         self.add(words[-1], '[SPLIT]')
#         self.add('[SPLIT]', words[0])
#
#     def add_to_dictogram(self, state, next_word):
#         if state not in self.data:
#             self.data[state] = Histogram()
#
#         self.data[state].update_word(next_word)
#
#     def generate_sentence(self):
#         current_state = self.random_start()
#         final_sentence = ''
#
#         while current_state != '[SPLIT]':
#             final_sentence += ' ' + current_state
#
#             states_histogram = self.data[current_state]
#             current_state = states_histogram.random_word()
#
#         return final_sentence[1:] + '.'
#
#     def random_start(self):
#         return self.data['[SPLIT]'].random_word()
#
#     def __str__(self):
#         return str(self.data)

from collections import deque

class Dictogram:
    # Don't forget to import deque
    # from collections import deque

    def __init__(self, words, order):
        self.order = order

        self.forwards = dict()
        self.backwards = dict()

        forwards_state = deque(words[0: order])
        backwards_state = deque(list(reversed(words[1: 1 + order])))

        self.sentence_starts = [tuple(forwards_state)]
        self.sentence_ends = []

        for i in range(order, len(words)):
            self.add_forward_word(i, forwards_state, words)
            self.add_backward_word(i, backwards_state, words)

        # Don't forget to set our last state to a split
        self.add(self.forwards, tuple(forwards_state), '[SPLIT]')

        if len(backwards_state) == self.order:
            self.sentence_ends.append(tuple(backwards_state))
            self.add(self.backwards, tuple(backwards_state), words[len(words) - self.order])

        self.add(self.backwards, tuple(reversed(words[0:self.order])), '[SPLIT]')

    def add_forward_word(self, i, forwards_state, words):
        if len(forwards_state) < self.order:
            forwards_state.append(words[i])

            if len(forwards_state) == self.order:
                self.sentence_starts.append(tuple(forwards_state))

            return

        next_word = words[i]

        if next_word[-1] == '.':
            next_word = next_word[:-1]

        self.add(self.forwards, tuple(forwards_state), next_word)

        forwards_state.popleft()
        forwards_state.append(next_word)

        # If the next word was a sentence end we set the last state equal to a split and clear our window
        if words[i][-1] == '.':
            self.add(self.forwards, tuple(forwards_state), '[SPLIT]')
            forwards_state.clear()

    def add_backward_word(self, i, state, words):
        if i + 2 > len(words):
            return

        if len(state) < self.order:
            if words[i - self.order - 1][-1] != '.':
                return

            for j in range(i - self.order + 1, i + 1):
                state_word = words[j]

                if state_word[-1] == '.':
                    if len(state) != self.order - 1:
                        state.clear()
                        return

                    state_word = state_word[:-1]

                state.insert(0, state_word)

            end = []
            for j in range(i - self.order * 2, i - self.order):
                word = words[j]

                if word[-1] == '.':
                    word = word[:-1]

                end.append(word)

            to_be_split = []
            for j in range(i - self.order, i):
                split_word = words[j]

                if split_word[-1] == '.':
                    split_word = split_word[:-1]

                to_be_split.insert(0, split_word)

            if len(state) < self.order:
                return

            self.add(self.backwards, tuple(to_be_split), '[SPLIT]')
            self.sentence_ends.append(tuple(reversed(end)))

        last_word = words[i - self.order]

        self.add(self.backwards, tuple(state), last_word)

        next_word = words[i + 1]
        if next_word[-1] == '.':
            next_word = next_word[:-1]

        state.pop()
        state.appendleft(next_word)

        if words[i][-1] == '.':
            state.clear()

    @staticmethod
    def add(data, state, next_word):
        if state not in data:
            data[state] = Histogram()

        data[state].update_word(next_word)

    def generate_sentence(self):
        current_state = deque(self.random_start())
        final_sentence = ''

        while current_state[-1] != '[SPLIT]':
            final_sentence += ' ' + current_state[0]

            states_histogram = self.forwards[tuple(current_state)]
            next_word = states_histogram.random_word()

            current_state.popleft()
            current_state.append(next_word)

        # We have to add the last state to the sentence
        return final_sentence[1:] + ' ' + ' '.join(tuple(current_state)[:-1]) + '.'

    def random_start(self):
        return self.sentence_starts[random.randint(0, len(self.sentence_starts) - 1)]

    def random_end(self):
        return self.sentence_ends[random.randint(0, len(self.sentence_ends) - 1)]

    def __str__(self):
        return str(self.forwards) + ' \n ' + str(self.backwards)


dictogram = Dictogram(words, 2)
print(dictogram.backwards)
print(dictogram.sentence_ends)
# print(dictogram.sentence_starts)
# print(dictogram.random_start())
# print(dictogram.generate_sentence())
