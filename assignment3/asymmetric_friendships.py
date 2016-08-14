'''
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 3: Thinking in MapReduce

Problem 4: Asymmetric Friendships

The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. Generate a list of all non-symmetric friend relationships (both (friend, person) and (person, friend) should be present).

Example:
$ python asymmetric_friendships.py friends.json

'''

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, friend)
    mr.emit_intermediate(friend, person)

def reducer(person, list_of_names):
    relations = dict()
    for name in list_of_names:
      relations[name] = relations.get(name,0)+1
    for name in relations:
      if relations[name] == 1:
        mr.emit([person, name])


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
