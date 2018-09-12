#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re


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
                words_from_input_file.extend(re.findall(r'(\w+)', line.replace(r'\n', ''), re.U))
                output_file.writelines(line)

            output_file.writelines("\n---weird---\n")
            output_file.writelines(" ".join(sorted(words_from_input_file)))
            
    except IOError:
        print("Problem with reading / writing to the file")
        


