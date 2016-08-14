'''
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 3: Thinking in MapReduce

Problem 5: Trim Strings of Nucleotides

Write a MapReduce query to remove the last 10 characters from each string of nucleotides, then remove any duplicates generated.

Example:
$ python unique_trims.py dna.json

'''

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    seq = record[1][:-10]
    mr.emit_intermediate(seq, 1)

def reducer(seq, list_of_seq):
    mr.emit(seq)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
