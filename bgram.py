import random
from collections import defaultdict


def train(dataset):
    bigram_counts = defaultdict(int)

    for name in dataset:
        name = '^' + name + '$'

        for i in range(len(name) - 1):
            curr_bigram = name[i:i + 2]
            bigram_counts[curr_bigram] += 1

    total_bigrams = sum(bigram_counts.values())

    bigram_probs = defaultdict(float)

    for bigram, count in bigram_counts.items():
        bigram_probs[bigram] = count / total_bigrams

    return bigram_probs


def generate_name(bi_probs):
    current_letter = '^'
    name = ''

    while current_letter != '$':
        possible_bigrams = [bigram for bigram in bi_probs if bigram.startswith(current_letter)]

        next_bigram = random.choices(possible_bigrams, [bi_probs[bigram] for bigram in possible_bigrams])[0]
        next_letter = next_bigram[1]

        name += next_letter
        current_letter = next_letter

    if name.__len__() < 4:
        name = generate_name(bi_probs)

    if name[name.__len__() - 1:] == '$':
        name = name[:name.__len__() - 1]

    return name