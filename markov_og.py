#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    f = open(corpus)
    text_block = f.read()
    stripped_block = text_block.strip()
    
    punctuation = ['%', '&', '(', ')', '*', '+', '/', '<', '=', '>', '@', '[', ']', '^', '`', '{', '|', '}', '~', '_']
   
    block_no_punctuation = ""
    
    # print stripped_block
    for character in stripped_block:
        if character not in punctuation:
            block_no_punctuation += character

    split_block = block_no_punctuation.split()

    # return split_block

    markov_dictionary = {}

    for i in range(len(split_block) -2):

        dictionary_key = (split_block[i], split_block[i+1])
        dictionary_value = split_block[i + 2]

        if dictionary_key not in markov_dictionary.keys():
            markov_dictionary[dictionary_key] = [dictionary_value]
        else:
            markov_dictionary[dictionary_key].append(dictionary_value)

    return markov_dictionary 

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # return "Here's some random text."

    start_key = random.choice(chains.keys()) # Still stunting,
    value = random.choice(chains[start_key]) # how
    silly_list = str(start_key[0]) + " " + str(start_key[1]) + " " # Still stunting,

    # for i in range(len(chains.keys())):
    #     print start_key
    #     print value

    while start_key in chains.keys():
        # print "This is our start_key: %s, %s" % (start_key[0], start_key[1])
        # print "This is our value: %s" % value
        # markov_phrase = start_key[0],start_key[1], value,
        # print value
        value = random.choice(chains[start_key])
        silly_list = silly_list + str(value) + " "
        start_key = (start_key[1], value) # start key s/b stunting, how
        if len(silly_list) > 100:
            break
        # silly_list.append(value,)
        # print start_key

    print silly_list

def main():
    args = sys.argv

    # Change this to read input_text from a file
    input_text = args[1]

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    # print random_text
    # print chain_dict

if __name__ == "__main__":
    main()
