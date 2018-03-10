import numpy as np

# Trump's speeches here: https://github.com/ryanmcdermott/trump-speeches
trump = open('speeches.txt', encoding='utf8').read()

corpus = trump.split()

word_dict = {}

for i in range(len(corpus)-1):
    if corpus[i] in word_dict.keys():
        word_dict[corpus[i]].append(corpus[i+1])
    else:
        word_dict[corpus[i]] = [corpus[i+1]]

first_word = np.random.choice(corpus)

chain = [first_word]

n_words = 50

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

print(' '.join(chain))
