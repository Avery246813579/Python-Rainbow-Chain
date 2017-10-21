from RainbowChain import MarkovModel
import pickle
import time

start_time = time.time()

print("Loading Markov Model\n===============")
raw_model = MarkovModel('data/hungergames1.txt', 1)

corpus_load = time.time()
print("Corpus Loaded in " + str(corpus_load - start_time) + "s\n")


print("Saving Markov Model\n===============")
with open('data/model.pickle', 'wb') as handle:
    pickle.dump(raw_model, handle, protocol=pickle.HIGHEST_PROTOCOL)

corpus_save = time.time()
print("Markov Model saved in " + str(corpus_save - corpus_load) + "s\n")

print("Time to Complete: " + str(corpus_save - start_time) + "s")
