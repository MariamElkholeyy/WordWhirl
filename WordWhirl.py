# This App Takes a word as input and calculates the number of possible permutations.

from collections import Counter
import math

def word_shuffler(word):
    letter_counts = Counter(word)
    num_permutations = math.factorial(len(word))
    
    for count in letter_counts.values():
        num_permutations //= math.factorial(count)
    
    return num_permutations

if __name__ == "__main__":
    word = input("Enter a word: ")
    num_permutations = word_shuffler(word)
    print(f"The word '{word}' can be shuffled in {num_permutations} different ways.")