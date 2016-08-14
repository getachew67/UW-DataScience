/*
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 2: SQL for Data Science Assignment

Problem 3: Working with a Term-Document Matrix

The reuters dataset can be considered a term-document matrix, which is an important representation for text analytics, and in this case, to compute the similarity of documents.

reuters.db database consists of a single table:
frequency(docid, term, count)

Example:
$ sqlite3 reuters.db < doc_similarity.sql

*/

-- (h)
SELECT d1.docid as doc1,
	   d2.docid as doc2,
	   sum(d1.count*d2.count) as similarity
FROM frequency d1, frequency d2
WHERE d1.term = d2.term
	and doc1 = '10080_txt_crude' and doc2 = '17035_txt_earn'
GROUP BY 1,2
ORDER BY 1,2
;

-- (i)
WITH q AS (
	SELECT 'q' as docid, 'washington' as term, 1 as count
	UNION
	SELECT 'q' as docid, 'taxes' as term, 1 as count
	UNION 
	SELECT 'q' as docid, 'treasury' as term, 1 as count
	)
SELECT d.docid,
	   sum(q.count*d.count) as similarity
FROM q, frequency d
WHERE q.term = d.term
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5
;