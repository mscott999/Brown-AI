#Import method 1.
import math
import random

print("result 1 is:", math.pow(2, 4))
print("result 2 is:", math.sqrt(16))
print("result 3 is", random.randint(0, 100))

names = ["name1", "name2", "name3", "name4", "name5"]
print("original names:", names)
random.shuffle(names)
print("names after shuffling:", names)
print("chosen name is:", random.choice(names))

#Import method 2.
#import math as m
#import random as r
#
#print("result 1 is:", m.pow(2, 4))
#print("result 2 is:", m.sqrt(16))
#print("result 3 is", r.randint(0, 100))
#
#names = ["name1", "name2", "name3", "name4", "name5"]
#print("original names:", names)
#r.shuffle(names)
#print("names after shuffling:", names)
#print("chosen name is:", r.choice(names))
#
#Import method 3.
#from math import pow, sqrt
#from random import randint, shuffle, choice
#
#print("result 1 is:", pow(2, 4))
#print("result 2 is:", sqrt(16))
#print("result 3 is", randint(0, 100))
#
#names = ["name1", "name2", "name3", "name4", "name5"]
#print("original names:", names)
#shuffle(names)
#print("names after shuffling:", names)
#print("chosen name is:", choice(names))