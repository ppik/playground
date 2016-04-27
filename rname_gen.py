#!/usr/bin/env python
# Random name generator from letters of an input string

import sys
import random

def gen_name(s, min_length=3):
    length = random.randint(min_length, len(s))
    return ''.join(random.sample(s, length))

if __name__ == "__main__":
    s = ' '.join(sys.argv[1:])
    while True:
        print(gen_name(s))
        if input() > '':
            break
        
    
