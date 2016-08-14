'''
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 3: Thinking in MapReduce

Problem 1: Inverted Index

Create an Inverted index. Given a set of documents, an inverted index is a dictionary where each word is associated with a list of the document identifiers in which that word appears.

Example:
$ python inverted_index.py books.json

'''

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    docid = record[0]
    text = record[1]
    words = text.split()
    for w in words:
      mr.emit_intermediate(w, docid)

def reducer(word, list_of_docids):
    mr.emit((word, list(set(list_of_docids))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
