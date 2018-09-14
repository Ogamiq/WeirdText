#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import numpy as np



def make_weird_sentence(line, words_from_line, weird_words):
    """
    Out of the line of text, words occuring in this line and corresponding weird words
    makes and returns new line of text that has it's words replaced with weird words 
    Example input: 'A very large sentence', ['A', 'very', 'large', 'sentence'], ['A', 'vrey', 'lrage', 'sneetcne']
    Example output: 'A vrey lrage sneetcne'
    """ 
    weird_sentence = line
    for i in range(len(words_from_line)):
        weird_sentence = weird_sentence.replace(words_from_line[i], weird_words[i])
    return weird_sentence


def make_weird_words(words_from_line):
    """
    Out of the list of words makes a list of weird words having corresponding indexes
    Weird word is the word with its inner letters shuffled. 
    Example input: ['A', 'very', 'large', 'sentence']
    Example output: ['A', 'vrey', 'lrage', 'sneetcne']
    """
    weird_words = []
    for i in range(len(words_from_line)):
        if len(words_from_line[i]) <= 3:
            weird_words.append(words_from_line[i])
        else:      
            letters_to_permute = list(words_from_line[i])[1: -1]
            permutation_counter = 0
            permuted_letters = np.random.permutation(letters_to_permute)
            while((permuted_letters == letters_to_permute).all() and permutation_counter <= 5):
                permuted_letters = np.random.permutation(letters_to_permute)
                permutation_counter += 1
            weird_word = words_from_line[i][0] + "".join(permuted_letters) + words_from_line[i][len(words_from_line[i]) -1]
            weird_words.append(weird_word)
    return weird_words

    
if __name__ == "__main__":
    """
    Based of the filename chosen using first command line argument 
    produces output in a separate file 'encoder_result.txt'
    that contains processed input file in a form:
    ---weird---
    processed lines
    ---weird---
    sorted list of all words used in the input file
    """
    if len(sys.argv) != 2:
        print("usage: python encoder.py ../data/to_encode*N*.txt, where *N* is a number of file to be encoded")
        sys.exit(1)

    try: 
        with open(sys.argv[1], "r") as input_file:
            output_file = open("../results/encoded.txt","w+")
            output_file.write('\n---weird---\n')

            words_from_input_file = []

            for line in input_file:
                words_from_line = re.findall(r'(\w+)', line.replace(r'\n', ''), re.U)
                words_from_input_file.extend(words_from_line)

                weird_words = make_weird_words(words_from_line)
                weird_sentence = make_weird_sentence(line, words_from_line, weird_words)
                output_file.writelines(weird_sentence)

            output_file.writelines("\n---weird---\n")
            output_file.writelines(" ".join(sorted(words_from_input_file, key=str.lower)))
            output_file.close()
                      
    except IOError:
        print("Problem with reading / writing to the file")
        


