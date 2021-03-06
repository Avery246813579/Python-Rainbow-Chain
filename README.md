# Python-Rainbow-Chain
The Rainbow Chain is a Markov Chain that can generate a sentence
forwards, backwards, and around a seed. This is great for generating
a sentence around a topic.

### Prerequisites
Before you can use Rainbow Chain, you need to install the following.
1. Python 2/3
2. Pip

## Installation
Install the latest stable build from PyPI

    pip install RainbowChain
    
## Running the tests

If you would like to test the project, run the [test files](test) using PyTest.  

## Usage
The best way to understand how to use the project is looking at
[the examples](examples). But here is a simple example.

    from RainbowChain import MarkovModel

    # Generates a model with an order of 2
    model = MarkovModel('path/to/corpus', 2)

    # Generate a random quote
    print(model.generate_sentence())

    # Generate a random quote with a seed
    print(model.generate_with_seed("Games"))
    
## Authors
* **Avery Durrant** - *Initial work* - [Avery246813579](https://github.com/Avery246813579)

See also the list of [contributors](https://github.com/Avery246813579/Python-Rainbow-Chain/contributors) who participated in this project.

## Speeding up load times
To get the most grammatically correct sentences we need a big corpus.
It our corpus gets too big and we have a high order (2+) Rainbow Chain,
it will take some time to construct our data. I suggest using something
like Pickle that stores your Rainbow Chain as a text file so you can
read it faster. It cut my load time in half.

#### Saving your Markov Model
    from RainbowChain import MarkovModel
    import pickle

    raw_model = MarkovModel('../static/data/raw_corpus.txt', 3)

    with open('../static/data/model.pickle', 'wb') as handle:
        pickle.dump(raw_model, handle, protocol=pickle.HIGHEST_PROTOCOL)

#### Loading your Markov Model
    model = None

    with open('static/data/model.pickle', 'rb') as handle:
        model = pickle.load(handle)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Coming Soon
1. Comment and Simplify Code. Add documentation.
1. Generate lower order sentences
1. Put sentence start and end into a Histogram
1. Publish Blog Post
1. Backoff suggestion since it doesnt work perfectly
