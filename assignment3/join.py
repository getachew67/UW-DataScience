'''
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 3: Thinking in MapReduce

Problem 2: Relational Join

Implement a relational join as a MapReduce query.

Example:
$ python join.py records.json

'''

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    orderid = record[1]
    mr.emit_intermediate(orderid, record)

def reducer(orderid, list_of_records):
    joined = list()
    order = [r for r in list_of_records if r[0] == 'order']
    line_item = [r for r in list_of_records if r[0] == 'line_item']
    for r1 in order:
      for r2 in line_item:
        mr.emit(r1+r2)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
