#! /usr/bin/env python3
import sys
import numpy as np

import random
from random import randint
#coding = utf-8


move = [
        [1,0],
        [1,1],
        [0,1],
        [-1,1],
        [-1,0],
        [-1,-1],
        [0,-1],
        [1,-1]
        ]


def JudgeWalk(mark):
    for i in range(mark.shape[0]):
        for j in range(mark.shape[1]):
            if mark[i][j] == 0:
                return False
    return True



if __name__=='__main__':
    X = int(sys.argv[1])
    Y = int(sys.argv[2])

    mark = np.zeros((X,Y),dtype=int)
    current_x = randint(0, X-1)
    current_y = randint(0, Y-1)

    num = 0
    while True:
        moving_idx = randint(0,7)
        next_x = current_x + move[moving_idx][0]
        next_y = current_y + move[moving_idx][1]

        while(next_x < 0 | next_y < 0 | next_x >= X | next_y >= Y):
            moving_idx = randint(0,7)
            next_x = current_x + move[moving_idx][0]
            next_y = current_y + move[moving_idx][1]

        mark[next_x][next_y] += 1

        current_x = next_x
        current_x = next_y
        num += 1

        label = JudgeWalk(mark)
        if label:
            print("所有的格子都访问用了:\t"+str(num)+" 次")
            for i in range(X):
                row_str = ''
                for j in range(Y):
                    row_str += str(mark[i][j])+' ,'
                print(row_str[:-1])

        #if num > 50000000:
        #    print("超过了运动次数！！！")
        #    for i in range(X):
        #        row_str = ''
        #        for j in range(Y):
        #            row_str += str(mark[i][j])+' ,'
        #        print(row_str[:-1])
        #    exit()
