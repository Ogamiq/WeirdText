# Weird Text - recruitment project

Python project that enable users to code and decode text in files

## Getting Started 

Clone this repository to your local machine and install all of the dependencies. 

Go to the src catalogue and run: 
- the encoder: python encoder.py ../data/to_encode*N*.txt, where *N* is a number of a file to be encoded
- the decoder: python decoder.py ../data/to_decode*N*.txt, where *N* is a number of a file to be decoded

You can find the results inside the results catalogue

### Prerequisites

Requires python3 and pip being installed 
Requires libraries: re, sys, numpy, pytest


## Running the tests

Go to the tests catalogue 

To execute all of the tests type: py.test -v
