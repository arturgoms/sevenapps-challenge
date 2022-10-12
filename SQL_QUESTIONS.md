1. What is the average total funding of all of the companies that the person with ID = ‘92a52877-8d5d-41a6-950f-1b9c6574be7a’ has worked at?

```sql
SELECT p.name, AVG(c.know_total_funding)
	FROM "work_history" AS w
JOIN company as c
	on c.id = w.company_id
JOIN "Person" as p
	on p.id = w.person_id
WHERE 
	w.person_id = '92a52877-8d5d-41a6-950f-1b9c6574be7a'
GROUP BY 
	p.name
```

Results:
| name         | avg      |
|--------------|----------|
| Douglas Gray | NULL	  |



2. How many companies are in the companies table that no people in the people table have worked for?

```sql
SELECT count(c.id) FROM company as c
LEFT JOIN  work_history as w
	on c.id = w.company_id
WHERE w.company_id is null
```

Results:
| count |
|-------|
| 9020  |

3. What are the ten most popular companies that these 1,000 people have worked for?

```sql
SELECT c.name FROM company as c
LEFT JOIN work_history as w
	on c.id = w.company_id
GROUP BY
	c.name
ORDER BY COUNT(c.id) DESC 
LIMIT 10;
```

Results:
| name                                        |
|---------------------------------------------|
| Microsoft                                   |
| Amazon Web Services (AWS)                   |
| Aruba, a Hewlett Packard Enterprise company |
| Intel Corporation                           |
| Motorola Mobility (a Lenovo Company)        |
| Big Apple Insurance Solutions               |
| METASKIN                                    |
| Workfront                                   |
| Journée Software                            |
| Cisco                                       |


4. Identify company founders in the people table. Then identify the companies that these people have founded and list the top three largest companies by headcount, along with the name of that company and the person ID of the founder(s)

```sql
SELECT p.name as person, c.name as company, c.head_count FROM company as c
LEFT JOIN work_history as w
	on c.id = w.company_id
LEFT JOIN "Person" as p
	on p.id = w.person_id
where title LIKE '%founder%'
GROUP BY 
	p.name, c.name, c.head_count
ORDER BY c.head_count DESC
LIMIT 3
```

Results:
| person          | company                  | head_count |
|-----------------|--------------------------|------------|
| Donna Harrison  | Dafiti                   | 2907       |
| Margaret Thomas | Clarify Health Solutions | 294        |
| Toni Boone      | Tempus Technologies, Inc | 133        |

5. For each person in the people table, identify their 2nd most recent job (if they only have 1 job, please exclude them). What is the average duration in years of employment across everyone’s 2nd most recent job? Additionally, how many people have had more than 1 job?

```sql
SELECT AVG(range) as AVERAGE_SECOND_RANGE_IN_YEARS, count(*) as PEOPLE_WITH_MORE_THEN_ONE_JOB FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY ID ORDER BY group_start_date DESC) AS rn
    FROM (
		SELECT b.id, wh.company_id, DATE_PART('year', wh.group_end_date::date) - DATE_PART('year', wh.group_start_date::date) AS range, wh.group_start_date, wh.group_end_date FROM (
				select p.id, count(w.person_id) from "Person" as p 
				LEFT JOIN work_history as w
					on w.person_id = p.id
				GROUP BY 
					p.id
				HAVING count(w.person_id) > 1
			) b
		LEFT JOIN work_history as wh
			on wh.person_id = b.id 
		group by b.id, wh.company_id, wh.group_start_date, wh.group_end_date
		) a
) x
WHERE rn = 2
```

Results:
| AVERAGE_SECOND_RANGE_IN_YEARS | PEOPLE_WITH_MORE_THEN_ONE_JOB |
|-------------------------------|-------------------------------|
| 2.9693094629156               | 904                           |
