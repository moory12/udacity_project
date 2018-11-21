import psycopg2


try:
	db = psycopg2.connect("dbname=news")		# connecting to the database 
except psycopg2.Error as e:
		print "Unable to connect!"
		print e.pgerror
		print e.diag.message_detail
else:
	print "Connected!"

	
c = db.cursor()

print("What are the most popular three articles of all time?")

#first query
c.execute(" select title,count(*) as views from articles,log where(slug = substring(path,10)) group by articles.title , substring(log.path,10) order by views DESC limit 3  ;");
result = c.fetchall()
for i in result:									#printing the result
	print i[0],str("----"),i[1],str("views")

print

print("Who are the most popular article authors of all time?")
	
#second query
c.execute(" select name,count(*) from articles,log,authors where((slug = substring(path,10)) and articles.author = authors.id  ) group by   articles.author,authors.id  order by count(*) DESC limit 4  ;");
result = c.fetchall()
for i in result:									#printing the result
	print i[0],str("----"),i[1],str("views")
	
print

print("On which days did more than 1% of requests lead to errors?")
print

#last query
c.execute(" select date(time),(( cast((select count(date(time)) from log where (log.status = '404 NOT FOUND') group by date(time) order by count(date(time)) DESC limit  1 ) as float)*100 /(select count(date(time)) from log where (log.status = '200 OK') group by date(time) order by count(date(time)) DESC limit 1) ))  as rate from log group by date(time) order by count(date(time)) DESC limit 1; ");
result = c.fetchall()
for i in result:									#printing the result
	print i[0],str("---"),i[1]	
	
	
