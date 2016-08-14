'''
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 3: Thinking in MapReduce

Problem 3: Count Friends

Consider a simple social network dataset consisting of a set of key-value pairs (person, friend) representing a friend relationship between two people. Implement a MapReduce algorithm to count the number of friends for each person.

Example:
$ python friend_count.py friends.json

'''

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0]
    mr.emit_intermediate(person, 1)

def reducer(person, list_of_friends):
    mr.emit((person, sum(list_of_friends)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
