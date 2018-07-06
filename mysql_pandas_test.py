#!/usr/bin/env python

#pip3 install --allow-external mysql-connector-python mysql-connector-python
#$ sudo service mysql start
#$ mysql -u dad -p
#password

# installing pandas and numpy
#apt-get update
#sudo apt-get install python-pandas
#sudo apt-get install python-numpy

#import the pandas library and alias it as pd
import pandas as pd

#import the number pi library and alias as np
import numpy as np

#import the mysql.connector
import mysql.connector
from mysql.connector import errorcode

#create an empty series object
s = pd.Series()
print(s)

#create a series object from a python Dictionary
floor1 = {1:"kitchen", 2:"living room", 3:"front room", 4:"bathroom", 5:"mud room"}
floor1Series = pd.Series(floor1)
print( floor1Series)

print( floor1Series[2] )
print( floor1Series[[2,4,5]] )

print("")
print("")

#create  database connection
cnx = mysql.connector.connect(user='dad', password='password',
                              host='127.0.0.1',
                              database='jumblo')

try:
    curs = cnx.cursor()
    
    print( "creating table")
    #table = "CREATE TABLE 'tempdat'('tdate' DATE, 'ttime' TIME, 'zone' TEXT,'temperature' NUMERIC)"
    
    table = "CREATE TABLE IF NOT EXISTS `tempdat`(`tdate` DATE, `ttime` TIME, `zone` TEXT,`temperature` NUMERIC)"
    curs.execute(table)
    print( "creating data")
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

    cnx.commit()
    print( "Data committed")

except mysql.connector.Error as err:
    print( "Error: the database connection failed")
    print(err.errno)
    print(err)

    
    #db.rollback()

cnx.close()
print( "done")

cnx = mysql.connector.connect(user='dad', password='password',
                              host='127.0.0.1',
                              database='jumblo')


print( "query the data")
print( "")

try:
        curs = cnx.cursor()
        curs.execute ("SELECT * FROM tempdat")

        print( "\nDate     	Time		Zone		Temperature" )
        print( "===========================================================" )

        for reading in curs.fetchall():
                print( str(reading[0])+"	"+str(reading[1])+" 	"+\
                        reading[2]+" 	"+str(reading[3]) )

        print( "===========================================================" )
        curs.execute ("SELECT * FROM tempdat WHERE temperature>%s", (str(20.0),) )
        for reading in curs.fetchall():
                print( str(reading[0])+"	"+str(reading[1])+" 	"+\
                        reading[2]+" 	"+str(reading[3]) )


except mysql.connector.Error as err:
        print( "Error: the query failed")
        print(err.errno)
        print(err)


cnx.close()
print( "done")