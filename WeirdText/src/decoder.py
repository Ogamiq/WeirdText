#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys 
import re



def make_words_translations(weird_words, normal_words):
    """
    Based on the list of weird words and sorted normal words generates the dictionary
	with the weird word as a value and the normal word (witch is it’s translation) as a key 
    Example input: ['Two', 'wrdos'], ['Two', 'words']
    Example output: {'Two':'Two', 'wrdos': 'words'}
    """
    assert(len(weird_words) == len(normal_words))
    translated_words = {}
    for k in weird_words:
        if k in translated_words: 
            continue
        else:
            for normal_word in normal_words:
                if k[0] == normal_word[0] and sorted(list(k)) == sorted(list(normal_word)):
                    translated_words[k] = normal_word
    return translated_words


if __name__ == "__main__":
    """
    Based of the filename chosen using first command line argument 
    produces output in a separate file 'decoder_result.txt'
    that contains processed input file. Requires a an input file to be in the form: 
    ---weird---
    lines that contains 'weird' words
    ---weird---
    sorted list of all words used in the input file
    The output is a best-try attempt to translate the lines with weird words in a form of 
    a lines of text that contain translated message
    """
    if len(sys.argv) != 2:
        print("usage: python decoder.py ../data/to_decode*N*.txt, where *N* is a number of file to be decoded")
    try:
        with open(sys.argv[1], "r") as input_file:
            weird_mark_counter = 0
            weird_text = []
            normal_words = []
            for line in input_file:
                if '---weird---' in line:       
                    weird_mark_counter += 1
                    continue
                if weird_mark_counter == 1: weird_text.extend([x for x in line])      
                if weird_mark_counter == 2: normal_words = line.split()              
                if weird_mark_counter >= 3: raise ValueError
        
        #TODO: add a result correctness evaluation here, as it's in the instructions
        # check for: empty arrays, invalid sorted word list, perhaps add a function evaluate_file_content that returns a boolean

        weird_words = words_from_line = re.findall(r'(\w+)', ''.join(weird_text).replace(r'\n', ''), re.U)
        translated_words = make_words_translations(weird_words, normal_words)
        #print(translated_words)

        output_file = open("../results/decoded.txt", "w+")
        output_file.write(str(translated_words))
        #TODO: after the job is finished, add the writing to the file here


    except IOError:
        print("Problem with reading / writing to the file")
    
    except ValueError:
        print("The content of the file seems to be invalid -> too many ---weird--- magic values")
    
    except AssertionError:
        print("Length of the 'weird words' and 'normal words' lists is not equal, that indicates problem with an input file")
