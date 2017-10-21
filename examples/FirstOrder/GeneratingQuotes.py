import pickle
import time

start_time = time.time()
print("Loading Markov Model w\Pickle\n===============")

model = None
with open('data/model.pickle', 'rb') as handle:
    model = pickle.load(handle)

corpus_load = time.time()
print("Corpus Loaded in " + str(corpus_load - start_time) + "s\n\n")

print("Regular Quotes\n===============")
for i in range(10):
    print(model.generate_sentence())

print("\n\nQuotes Seeded with Hunger\n===============")
for i in range(10):
    print(model.generate_with_seed("hunger"))

print("\n\nQuotes Seeded with Game\n===============")
for i in range(10):
    print(model.generate_with_seed("Games"))

