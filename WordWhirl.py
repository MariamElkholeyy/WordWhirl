# This App Takes a word as input and calculates the number of possible permutations.

import itertools

def word_shuffler(word):
    permutations = itertools.permutations(word)
    num_permutations = len(list(permutations))
    return num_permutations

if __name__ == "__main__":
    word = input("Enter a word: ")
    num_permutations = word_shuffler(word)
    print(f"The word '{word}' can be shuffled in {num_permutations} different ways.")
