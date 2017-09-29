#!/usr/bin/env python
#coding:utf-8
import psycopg2
import datetime
# Connect to an existing database
DB_NAME = "news"

# 1. What are the most popular three articles of all time?
query1 = "select * from topthree"

# 2. Who are the most popular article authors of all time?
query2 = "select * from mpaa"

# 3. On which days did more than 1% of requests lead to errors?
query3 = "select * from error_percent"

def popular_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query1)
    rows = c.fetchall()
    for i in range(len(rows)):
        title = rows[i][0]
        views = rows[i][1]
        print("%s--%d" % (title,views))
    db.close()


def popular_authors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query2)
    rows = c.fetchall()
    db.close()
    for i in range(len(rows)):
        name = rows[i][0]
        views = rows[i][1]
        print("%s--%d" % (name, views))


def error_percent():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query3)
    rows = c.fetchall()
    db.close()
    for i in range(len(rows)):
        date = rows[i][0]
        percent = rows[i][1]
        print("%s--%d %%"%(date,percent))



if __name__ == "__main__":
    print("The top 3 articles")
    popular_articles()
    print("\n")
    print("The most popular author:")
    popular_authors()
    print("\n")
    print(" which days did more than 1% of requests lead to errors:")
    error_percent()
