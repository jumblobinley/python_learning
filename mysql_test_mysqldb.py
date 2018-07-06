have only gotten this far…..Accessing a MySQL database with Python
I'm going to use Python to populate the database. As in the previous examples, I'm going to create sample data from one day ago, 12 hours ago and now, and I'm going to record temperatures in three different zones.
This Python code is the start of my script:

#!/usr/bin/env python

import MySQLdb


db = MySQLdb.connect("localhost", "monitor", "password", "temps")
curs=db.cursor()



I imported the MySQLdb python module and connected to it with the user name and password that I set up in the shell. The following code then inserts records into the database:

# note that I'm using triplle quotes for formatting purposes
# you can use one set of double quotes if you put the whole string on one line
try:
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'kitchen', 21.7)""")
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'greenhouse', 24.5)""")
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'garage', 18.1)""")

    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW() - INTERVAL 12 HOUR, 'kitchen', 20.6)""")
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW() - INTERVAL 12 HOUR, 'greenhouse', 17.1)""")
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW() - INTERVAL 12 HOUR, 'garage', 16.2)""")

    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW(), 'kitchen', 22.9)""")
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW(), 'greenhouse', 25.7)""")
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW(), 'garage', 18.2)""")

    db.commit()
    print "Data committed"

except:
    print "Error: the database is being rolled back"
    db.rollback()

If there's an error during any of these SQL commands, or if there's an error while committing the changes, the changes will be rolled back. This can be simplified using a Python context manager:

with db:
    curs.execute ("""INSERT INTO tempdat
            values(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'kitchen', 21.7)""")
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'greenhouse', 24.5)""")
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'garage', 18.1)""")

    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW() - INTERVAL 12 HOUR, 'kitchen', 20.6)""")
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW() - INTERVAL 12 HOUR, 'greenhouse', 17.1)""")
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW() - INTERVAL 12 HOUR, 'garage', 16.2)""")

    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW(), 'kitchen', 22.9)""")
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW(), 'greenhouse', 25.7)""")
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW(), 'garage', 18.2)""")


This will automatically handle commit and rollback operations.
Getting data from the database
Once data has been inserted into the database, we need to be able to retrieve it. We can do this using the SQL select command. The execute function runs the SQL query, and the fetchall function returns a list of records that matched the query:

curs.execute ("SELECT * FROM tempdat")

print "\nDate     	Time		Zone		Temperature"
print "==========================================================="

for reading in curs.fetchall():
    print str(reading[0])+"	"+str(reading[1])+" 	"+\
                reading[2]+" 	"+str(reading[3])



The for loop iterates through the list of results. Each record is a list of values. Note that the time and the temperature values have to be converted to a string before they can be appended to the result string. This code prints the contents of the entire database as a table:

Date     	Time		Zone		Temperature
===========================================================
2013-09-09	14:41:46 	kitchen  	21.7
2013-09-09	14:41:46 	greenhouse  	24.5
2013-09-09	14:41:46 	garage  	18.1
2013-09-10	2:41:46 	kitchen  	20.6
2013-09-10	2:41:46 	greenhouse  	17.1
2013-09-10	2:41:46 	garage  	16.2
2013-09-10	14:41:46 	kitchen  	22.9
2013-09-10	14:41:46 	greenhouse  	25.7
2013-09-10	14:41:46 	garage  	18.2



We can use the WHERE keyword to attach conditions to a query. In this example, I'm going to search for records where the temperature is above 20.0 degrees:

curs.execute ("SELECT * FROM tempdat WHERE temp>%s", (str(20.0),))



Note that it's important not to use string substitution to insert parameters into the query as this makes it easier for people to inject malicious SQL code into a query. This query does the same thing, but it's less secure:

curs.execute ("SELECT * FROM tempdat WHERE temp>%s" % str(20.0))



In this example, the variable is unconditionally inserted into the query. In the previous one, the query and the parameter are passed to the MySQL library, which checks to see if the parameter is safe before inserting it.
The output from this query is

Date     	Time		Zone		Temperature
===========================================================
2013-09-09	14:41:46 	kitchen  	21.7
2013-09-09	14:41:46 	greenhouse  	24.5
2013-09-10	2:41:46 	kitchen  	20.6
2013-09-10	14:41:46 	kitchen  	22.9
2013-09-10	14:41:46 	greenhouse  	25.7



At the end of the script, we close the connection to the database:

db.close()



See also: http://dev.mysql.com/doc/refman/5.5/en/sql-syntax.html.

