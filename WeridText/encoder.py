#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re


def make_weird_sentence(line, words_from_line, weird_words):
    weird_sentence = line
    for i in range(len(words_from_line)):
        weird_sentence = weird_sentence.replace(words_from_line[i], weird_words[i])
    return weird_sentence


def make_weird_words(words_from_line):
    weird_words = []
    for i in range(len(words_from_line)):
        weird_words.append('{0}'.format(i))
    return weird_words

    
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("usage: python encoder.py file_to_encode.txt")
        sys.exit(1)

    try: 
        with open(sys.argv[1], "r") as input_file:
            output_file = open("encoder_result.txt","w+")
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

    except IOError:
        print("Problem with reading / writing to the file")
        


