#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimumMovement' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY obstacleLanes as parameter.
#

def minimumMovement(obstacleLanes):
    # Write your code here
    
    return 0

Obstacles_lanes = [2,1,2]
currpos = 0
nextpos = 1
position = 0
lanes_range = 3
Lanes = list(range(1,lanes_range))

for value in range(0,len(Obstacles_lanes)):
    if value == len(Obstacles_lanes):
        break
    else:
        currpos = Lanes[Obstacles_lanes[value]]
        nextpos = Lanes[Obstacles_lanes[value+1]]
        list_pos = [currpos,nextpos]
        
