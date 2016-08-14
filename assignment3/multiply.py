'''
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 3: Thinking in MapReduce

Problem 6: Matrix Multiplication

Design a MapReduce algorithm to compute the matrix multiplication A x B. A and B are in a sparse matrix format, where each record is of the form i, j, value.

Example:
$ python multiply.py matrix.json

'''

import MapReduce
import sys

# Assuming matrix dimensions are known
# A is MxN matrix, and B is NxK matrix
M, N, K = 5, 5, 5

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    if record[0] == 'a':
      for j in range(5):
        mr.emit_intermediate((record[1],j), record)
    elif record[0] == 'b':
      for i in range(5):
        mr.emit_intermediate((i,record[2]), record)

def reducer(cell, list_of_records):
    value = 0
    for k in range(5):
      try:
        a_ik = [r[3] for r in list_of_records if r[0] == 'a' and r[2] == k]
        b_kj = [r[3] for r in list_of_records if r[0] == 'b' and r[1] == k]
        value += a_ik[0]*b_kj[0]
      except: continue

    mr.emit((cell[0], cell[1], value))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
