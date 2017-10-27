from RainbowChain import Dictogram

words = 'One fish two fish red fish blue fish. One dog two dog red dog blue dog'.split()

d = Dictogram(words, 3)

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
print(d.sentence_ends)
# {('dog', 'blue'): Histogram[{'dog': 1}],
# ('blue', 'dog'): Histogram[{'red': 1}],
# ('dog', 'red'): Histogram[{'dog': 1}],
# ('red', 'dog'): Histogram[{'two': 1}],
# ('dog', 'two'): Histogram[{'dog': 1}],
# ('two', 'dog'): Histogram[{'One': 1}],
# ('dog', 'One'): Histogram[{'[SPLIT]': 1}],
# ('fish', 'blue'): Histogram[{'fish': 1}],
# ('blue', 'fish'): Histogram[{'red': 1}],
# ('fish', 'red'): Histogram[{'fish': 1}],
# ('red', 'fish'): Histogram[{'two': 1}],
# ('fish', 'two'): Histogram[{'fish': 1}],
# ('two', 'fish'): Histogram[{'One': 1}]}

# [('dog', 'blue'), ('fish', 'blue')]


# {('two', 'fish'): [Histogram: {'One': 1}],
# ('fish', 'fish'): [Histogram: {'fish': 1}],
# ('fish', 'red'): [Histogram: {'two': 1}],
# ('red', 'fish'): [Histogram: {'fish': 1}],
# ('fish', 'blue'): [Histogram: {'red': 1}],
# ('blue', 'fish'): [Histogram: {'fish': 1}],
# ('dog', 'One'): [Histogram: {'[SPLIT]': 1}],
# ('dog', 'two'): [Histogram: {'One': 1}],
#  ('two', 'dog'): [Histogram: {'dog': 1}],
# ('dog', 'red'): [Histogram: {'two': 1}],
# ('red', 'dog'): [Histogram: {'dog': 1}],
# 2('dog', 'blue'): [Histogram: {'red': 1}], ('blue', 'dog'): [Histogram: {'dog': 1}], ('fish', 'One'): [Histogram: {'[SPLIT]': 1}]}
# [('fish', 'One'), ('blue', 'dog')]



# {('dog',): Histogram[{'blue': 1, 'red': 1, 'two': 1, 'One': 1}],
# ('blue',): Histogram[{'dog': 1, 'fish': 1}],
# ('red',): Histogram[{'dog': 1, 'fish': 1}],
# ('two',): Histogram[{'dog': 1, 'fish': 1}],
# ('One',): Histogram[{'[SPLIT]': 1}],
# ('fish',): Histogram[{'blue': 1, 'red': 1, 'two': 1, 'One': 1}]}
# [('dog',), ('fish',)]


# {('fish',): [Histogram: {'One': 1, 'two': 1, 'red': 1, 'blue': 1}],
# {('two', 'fish'): [Histogram: {'One': 1}], ('fish', 'fish'): [Histogram: {'fish': 1}], ('fish', 'red'): [Histogram: {'two': 1}], ('red', 'fish'): [Histogram: {'fish': 1}], ('fish', 'blue'): [Histogram: {'red': 1}], ('blue', 'fish'): [Histogram: {'fish': 1}], ('dog', 'One'): [Histogram: {'[SPLIT]': 1}], ('dog', 'two'): [Histogram: {'One': 1}], ('two', 'dog'): [Histogram: {'dog': 1}], ('dog', 'red'): [Histogram: {'two': 1}], ('red', 'dog'): [Histogram: {'dog': 1}], ('dog', 'blue'): [Histogram: {'red': 1}], ('blue', 'dog'): [Histogram: {'dog': 1}], ('fish', 'One'): [Histogram: {'[SPLIT]': 1}]}
# [('fish', 'One'), ('blue', 'dog')]









# {('dog', 'blue', 'dog'): Histogram[{'red': 1}],
# ('blue', 'dog', 'red'): Histogram[{'dog': 1}],
# ('dog', 'red', 'dog'): Histogram[{'two': 1}],
# ('red', 'dog', 'two'): Histogram[{'dog': 1}],
# ('dog', 'two', 'dog'): Histogram[{'One': 1}],
# ('two', 'dog', 'One'): Histogram[{'[SPLIT]': 1}],
# ('fish', 'blue', 'fish'): Histogram[{'red': 1}],
# ('blue', 'fish', 'red'): Histogram[{'fish': 1}],
# ('fish', 'red', 'fish'): Histogram[{'two': 1}],
# ('red', 'fish', 'two'): Histogram[{'fish': 1}],
# ('fish', 'two', 'fish'): Histogram[{'One': 1}]}

# [('dog', 'blue', 'dog'), ('fish', 'blue', 'fish')]
