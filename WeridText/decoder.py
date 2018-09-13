#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys 
import re




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python encoder.py file_to_decode.txt")
        sys.exit(1)
    try:
        with open(sys.argv[1], "r") as input_file:
            weird_mark_counter = 0
            weird_text = []
            sorted_words = []
            for line in input_file:
                if '---weird---' in line:       
                    weird_mark_counter += 1
                    continue
                if weird_mark_counter == 1: weird_text.extend([x for x in line])      
                if weird_mark_counter == 2: sorted_words = line.split()              
                if weird_mark_counter >= 3: raise ValueError
      
        output_file = open("decoder_result.txt", "w+")
        #output_file.write(str(weird_text) + '\n' + sorted_words.join)
        print(weird_text)
        print(sorted_words)
        


    except IOError:
        print("Problem with reading / writing to the file")
    
    except ValueError:
        print("Couldn't extract values for the text file")
