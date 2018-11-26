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
   
##Set up instructions
	first you need to install virtualBox then you need to install Vagrant.
	aftre that you need to run the virtualBox by typing Vagrant up 
	then type Vagrant ssh to run the vagrant
	now in order to run test.py you need to move the file to the vagrant folder
	along with the database file 
	and finally just type python test.py 
	