#! /usr/bin/python3
"""
Python word counter.

Usage: python3 word_counter.py <file_name>

For this implementation, a word is defined as collection of characters separated by spaces. Each word is transformed into lower-case and counted towards the final result.

Due to this definition of word "the", and "The" are considered to be the same word, while "the" and "the." are not.
"""
import random
import sys
from collections import defaultdict


def get_words_frequency_from_file(file_path):
    with open(file_path) as words_file:
        words_frequency = defaultdict(int)
        total_words = 0

        for line in words_file.readlines():
            for word in line.split():
                words_frequency[word.lower()] += 1
                total_words += 1

        return words_frequency, total_words


# Reverse quicksort implementation
def sort_words_frequency(words_frequency_tuples):
    if len(words_frequency_tuples) < 2:
        return words_frequency_tuples

    pivot_index = random.randint(0, len(words_frequency_tuples) - 1)
    pivot = words_frequency_tuples[pivot_index][1]

    high, same, low = [], [], []

    for word_frequency_tuple in words_frequency_tuples:
        if word_frequency_tuple[1] > pivot:
            high.append(word_frequency_tuple)
        elif word_frequency_tuple[1] == pivot:
            same.append(word_frequency_tuple)
        else:
            low.append(word_frequency_tuple)

    return sort_words_frequency(high) + same + sort_words_frequency(low)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: word_counter.py <file_path>")
        sys.exit(-1)

    file_path = sys.argv[1]

    words_frequency, total_words = get_words_frequency_from_file(file_path)
    words_frequency_as_tuples = list(words_frequency.items())
    sorted_words_frequency = sort_words_frequency(words_frequency_as_tuples)

    print("Top 10 Words:")
    for word, frequency in sorted_words_frequency[:10]:
        print(f"{word} {frequency}")

    print(f"Total Words: {total_words}")
