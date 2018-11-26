#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import psycopg2
from datetime import datetime

DBNAME = "news"


def connect(database_name):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except psycopg2.Error as err:
        print("Unable to connect to database")
        sys.exit(1)  # The easier method - exit the program


def answer1(cursor):
    """Answer the first question ..."""
    query = """  SELECT title,
                count(*) AS views
                FROM articles,
                log
                WHERE (slug = substring(PATH, 10))
                GROUP BY articles.title,
                substring(log.path, 10)
                ORDER BY views DESC
                LIMIT 3 ;"""

    print("Question 1: What are the most popular three articles of all time?")
    print("\n")
    cursor.execute(query)
    result = cursor.fetchall()
    for title, views in result:
        print("{} -- {} views".format(title, views))


def answer2(cursor):
    """Answer second question ..."""
    query = """select name,count(*) from articles,log,authors
                where((slug = substring(path,10))
                and articles.author = authors.id)
                group by articles.author,authors.id
                order by count(*) DESC limit 4;"""

    print("Question 2: Who are the most popular article authors of all time?")
    print("\n")
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:  # printing the result
        print
        i[0], str("----"), i[1], str("views")


def answer3(cursor):
    """Answer the third first question ..."""
    query = """ select date(time),
                (( cast((select count(date(time))
                from log where (log.status = '404 NOT FOUND')
                group by date(time)
                order by count(date(time)) DESC limit  1 ) as float)*100/
                (select count(date(time))
                from log where (log.status = '200 OK')
                group by date(time)
                order by count(date(time)) DESC limit 1)))as rate
                from log
                group by date(time)
                order by count(date(time)) DESC limit 1;"""

    print("Question 3: What are the most popular three articles of all time?")
    print("\n")
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:  # printing the result
        print
        i[0], str("---"), i[1]


def run():
    print("Running reporting tools...\n")
    db, cursor = connect(DBNAME)

    answer1(cursor)
    print("\n")

    answer2(cursor)
    print("\n")

    answer3(cursor)
    print("\n")


if __name__ == '__main__':
    run()
