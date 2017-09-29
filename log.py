#!/usr/bin/env python
import psycopg2
# Connect to an existing database
DB_NAME = "news"

# 1. What are the most popular three articles of all time?
query1 = "select * from topthree"

# 2. Who are the most popular article authors of all time?
query2 = "select * from mpaa"

# 3. On which days did more than 1% of requests lead to errors?
query3 = "select * from error_percent"


def popular_articles():
    db = psycopg2.Connect("dbname=news")
    c = db.cursor()
    c.execute(query1)
    rows = c.fetchall()
    print rows
    db.close（）
