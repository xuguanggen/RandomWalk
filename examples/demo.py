#! /usr/bin/env python3
import sys
import random
from random import randint
#coding = utf-8


move = [
        [-1,1],  # northeast
        [0,1],   # east
        [1,1],   # southeast
        [1,0],   # south
        [1,-1],  # southwest
        [0,-1],  # west
        [-1,-1], # northwest
        [-1,1]   # north
        ]



if __name__=='__main__':
    X = int(sys.argv[1])
    Y = int(sys.argv[2])

    current_x = randint(0, X-1)
    current_y = randint(0, Y-1)
    print("X length:\t"+str(X))
    print("Y length:\t"+str(Y))
    print("x:\t"+str(current_x))
    print("y:\t"+str(current_y))
