## Project: Logs Analysis
This project is for solving 3 querys 
 ### What are the most popular three articles of all time?
 ### Who are the most popular article authors of all time?
 ### On which days did more than 1% of requests lead to errors?
 
## The database
 the database called news which contains 3 tables
 ### articles
	which have 7 columns (author , title , slug , lead , body , time ,id)
 ### authors
	which have 3 columns (name , bio , id)
 ### log
	which have 6 columns (path , ip , method , status , time , id)

## Requirements
	- Vagrant
	- VirtualBox
	- the database file 
	- Python
	- PostgreSQL
	- Psycopg2 library
   

in order to run the code first you need to run vagrant and make sure you have the database file and the test.py file in the vagrant
then write in the commend python test.py to run the file.