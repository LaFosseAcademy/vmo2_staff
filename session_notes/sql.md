# SQLite

## Commands

### Opening a DB file
```sql
sqlite3 <file-name>.db
```

### Exiting SQL
```sql
.quit
```

### See tables in DB
```sql
.tables
```

### See table schema
`PRAGMA table_info(<table-name>);`

### See column headings on DB
```sql
.headers on
```

### Typical SQL Grammer
```sql
SELECT
FROM
LEFT JOIN
ON
WHERE
GROUP BY
HAVING
ORDER BY
```

### Request all data
```sql
SELECT * FROM student_results;
```

### Filtering data
```sql
SELECT name, score
FROM student_results
WHERE score >= 95;
```


### Conditions
```sql
SELECT name, score
FROM student_results
WHERE gender = 'M' 
AND school = 'Greenfield Secondary' 
AND (score >= 85 OR score <= 50);
```

### ORDER BY and LIMIT
```sql
SELECT *
FROM student_results
ORDER BY score DESC
LIMIT 10;
```

### AGGREGATE FUNCTIONS
```sql
SELECT COUNT(*) FROM student_results;

SELECT AVG(score) FROM student_results;

SELECT SUM(score) 
FROM student_results
WHERE school = 'Greenfield Secondary';
```

### Tierd Query
- The inner select returns a subsection of the table. Age information of the top 15 students female students.
- The outer SELECT returns the average value of those ages. 

```sql
SELECT AVG(age)
FROM (
    SELECT age
    FROM student_results
    WHERE gender = 'F'
    ORDER BY score DESC
    LIMIT 15
);
```


### JOINS
```sql
SELECT student.name, exam.subject, exam.score
FROM students as student
LEFT JOIN student_subjects as exam
ON student.student_id = exam.student_id
WHERE exam.subject  = 'History' AND exam.score > 95;
```







# CHALLENGES

## SQL Challenges 1

Use SQL to query the **student_results** table to answer the following questions.
1. Who were the students who scored 100 marks?

2. What's the average age of the students?

3. How many students attend Oakwood Grammar School?

4. How many students are 16 or under?

5. What's the average score for Male students?

6. What's the name of the youngest student to sit their exam?

7. What school had the most pupils sit their exam?

8. What's the average score for the lowest performing 20 boys at Northbridge High School?



## SQL Challenges 1 Solutions
1. Who were the students who scored 100 marks?
- `SELECT name, score FROM student_results WHERE score = 100;`
```sql
name|score
Mia Garcia|100
Liam Johnson|100
Sophia Johnson|100
Emma Miller|100
James Clark|100
Lucas Wilson|100
Grace Thomas|100
Olivia Moore|100
Abigail Smith|100
William Smith|100
```

2. What's the average age of the students?
- `SELECT AVG(age) FROM student_results;`
- 17.07

3. How many students attend Oakwood Grammar School?
- `SELECT COUNT(*) FROM student_results WHERE school = 'Oakwood Grammar School';`
- 124

4. How many students are 16 or under?
- `SELECT COUNT(*) FROM student_results WHERE age <= 16;`
- 190

5. What's the average score for Male students?
- `SELECT AVG(score) FROM student_results WHERE gender = 'M';`
- 66.5

6. What's the name of the youngest student to sit their exam?
- `SELECT name FROM student_results ORDER BY age LIMIT 1;`
- Jack Martin

7. What school had the most pupils sit their exam?
```sql
SELECT school, COUNT(school)
FROM student_results
GROUP BY school;
```
- Oakwood Grammar School | 124

8. What's the average score for the lowest performing 5 boys at Northbridge High School
```sql
SELECT AVG(score)
FROM (
  SELECT score
  FROM student_results
  WHERE gender = 'M' AND school = 'Northbridge High School'
  ORDER BY score
  LIMIT 5
);
```
- 36.6



## SQL Challenges 2

1. Find the average scores for male and female students

2. Rank the subjects the students did the best at from best to worst

### SQL Challenges 2 Solutions

1. Find the average scores for male and female students
```sql
SELECT student.gender, ROUND(AVG(exam.score),2)
FROM students AS student
JOIN student_subjects AS exam
ON student.student_id = exam.student_id
GROUP BY student.gender;
```

```sql
F|67.68
M|66.44
```

2. Rank the subjects the students did the best at from best to worst

```sql
SELECT subject, ROUND(AVG(score), 2)
FROM student_subjects
GROUP BY subject
ORDER BY AVG(score) DESC;
```

```sql
History|71.87
Science|70.0
English|65.1
Math|61.1
```

