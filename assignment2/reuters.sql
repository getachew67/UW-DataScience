/*
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 2: SQL for Data Science Assignment

Problem 1: Inspecting the Reuters Dataset and Basic Relational Algebra

reuters.db database consists of a single table:
frequency(docid, term, count)

Example:
$ sqlite3 reuters.db < reuters.sql

*/

-- (a)
SELECT count(*) FROM frequency
WHERE docid = '10398_txt_earn';


-- (b)
SELECT count(*) FROM (	
	SELECT term FROM frequency
	GROUP BY term
	HAVING docid = '10398_txt_earn'
		and count(*) = 1
	) b;

-- (c)
SELECT count(*) FROM (
	SELECT term FROM frequency
	GROUP BY term
	HAVING docid = '10398_txt_earn'
		and count(*) = 1

	UNION

	SELECT term FROM frequency
	GROUP BY term
	HAVING docid = '925_txt_trade'
		and count(*) = 1
	) c;

-- (d)
SELECT count(*) FROM (
	SELECT docid, count(*) FROM frequency
	WHERE term = 'law' or term = 'legal'
	GROUP BY docid
	) d;

-- (e)
SELECT count(*) FROM (
	SELECT docid, sum(count) as term_count FROM frequency
	GROUP BY docid
	HAVING term_count > 300
	) e;

-- (f)
SELECT count(*) FROM (
	SELECT DISTINCT docid FROM frequency
	WHERE term = 'transactions'

	INTERSECT

	SELECT DISTINCT docid FROM frequency
	WHERE term = 'world'
	) f;