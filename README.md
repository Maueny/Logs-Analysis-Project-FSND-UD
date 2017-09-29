# Logs-Analysis-Project-FSND-UD
Aim of this project is to print report based on data in database by using python(2.7.10) and PostgreSQL.

## How to install
1.Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)<br>
2.Download or clone from github [fullstack-nandegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)<br>
3.Get newsdata.sql in your vagrant directory 

* The **authors** table includes information about the authors of articles.
* The **articles** table includes the articles themselves.
* The **log** table includes one entry for each time a user has accessed the site.

### How to run<br>
1. change directory to vagrant directory then<br>
2. **vagrant up** command to run the vagrant on vm<br>
3. **vagrant ssh** to login into vm<br>
4. change directory to vagrant<br>
5. use command **psql -d news -f newsdata.sql** to load database<br>
6. use command **python log.py** to run the programm<br>

### Views Made
1. What are the most popular three articles of all time?
#### topthree
```
CREATE VIEW topthree 
AS SELECT title, 
          count(title) 
          AS views 
FROM log, 
     articles 
WHERE log.path 
      LIKE concat('/article/', articles.slug)
GROUP BY title 
ORDER BY views desc
LIMIT 3;
```

2. Who are the most popular article authors of all time? 
#### mpaa
```
CREATE VIEW mpaa AS
SELECT authors.name, 
       count(articles.author) 
       AS views 
FROM log, 
     articles, 
     authors
WHERE log.path 
      LIKE concat('/article/', articles.slug) 
      AND articles.author = authors.id
GROUP BY authors.name
ORDER BY views desc
LIMIT 1;
```

3.On which days did more than 1% of requests lead to errors?
#### total_request/error_request/error_percent
```
CREATE VIEW total_request AS
SELECT count(*) 
       AS count, 
       date(time) AS date 
FROM log 
GROUP BY date 
ORDER BY count DESC;

CREATE VIEW error_request AS
SELECT count(*) AS count, 
       date(time) AS date 
FROM log 
WHERE status != '200 OK'
GROUP BY date
ORDER BY count DESC;

CREATE VIEW error_percent AS
SELECT total_request.date,
       ROUND(100.0* error_request.count/total_request.count)
FROM total_request, 
     error_request
WHERE total_request.date = error_request.date
ORDER BY round DESC
LIMIT 1;
```
