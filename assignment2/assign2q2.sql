/*
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 2: SQL for Data Science Assignment

Problem 2: Matrix Multiplication in SQL

For advanced databases execute queries in parallel automatically. So it can be quite efficient to process a very large sparse matrix --- millions of rows or columns --- in a database.

matrix.db database consists of two matrices A and B:

A(row_num, col_num, value)
B(row_num, col_num, value)

Example:
$ sqlite3 matrix.db < assign2q2.sql

*/

-- (g)
SELECT A.row_num as row_num,
	   B.col_num as col_num,
	   sum(A.value*B.value) as value
FROM A, B
WHERE A.col_num = B.row_num
GROUP BY 1,2
ORDER BY 1,2
HAVING sum(A.value*B.value) != 0
;