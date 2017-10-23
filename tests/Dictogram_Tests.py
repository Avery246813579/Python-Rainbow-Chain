from RainbowChain import Dictogram
words = 'One fish two fish red fish blue fish.'.split()

d = Dictogram(words, 2)

# file_reader = FileParser('static/test_data.txt')

# test_dict = Dictogram(file_reader.words, 3)
# print(test_dict)
# print(str(test_dict.sentence_starts))
# print(str(test_dict.sentence_ends))

# with open('data.pickle', 'wb') as handle:
#     pickle.dump(test_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

# with open('data.pickle', 'rb') as handle:
#     test_dict = pickle.load(handle)
#     print(test_dict.random_forward_key())
#
# print("HI")


print(d.backwards)
# {('fish', 'blue'): Histogram[{'fish': 1}],
# ('blue', 'fish'): Histogram[{'red': 1}],
# ('fish', 'red'): Histogram[{'fish': 1}],
# ('red', 'fish'): Histogram[{'two': 1}],
# ('fish', 'two'): Histogram[{'fish': 1}],
# ('two', 'fish'): Histogram[{'One': 1}]}



# {('two', 'fish'): [Histogram: {'fish': 1}],
# ('fish', 'red'): [Histogram: {'two': 1}],
#  ('red', 'fish'): [Histogram: {'fish': 1}],
# ('fish', 'blue'): [Histogram: {'red': 1, 'fish': 1}]}


