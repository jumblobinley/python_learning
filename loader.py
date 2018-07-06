#!/usr/bin/env python

#pip3 install --allow-external mysql-connector-python mysql-connector-python

#import the mysql.connector
#import mysql.connector
#from mysql.connector import errorcode

class Row:
    """This class encapsulates all data associated with one row from file"""
    
    def __init__(self,full_line):
        """default constructur loads a row from one string in the format 'index,qty_ord,qty_ship,part,m_part,price,extended' """
        self.full_line = full_line
        elements = full_line.split(",")
        #print(elements)
        self.index=elements[0]
        self.qty_ord=elements[1]
        self.qty_ship=elements[2]
        self.part=elements[3]
        self.m_part=elements[4]
        self.price=elements[5]
        self.extended=elements[6]
        
    def __repr__(self):
        return "Row(%s, %s, %s, %s, %s, %s, %s)" % (self.index,self.qty_ord,self.qty_ship,self.part,self.m_part,self.price,self.extended)

    @classmethod
    def row_from_columns(cls,index,qty_ord,qty_ship,part,m_part,price,extended):
        """ this is class specifi factory method - not an isntance method - which will create an instance of a Row and return it full of data """
        newrow = cls(" , , , , , , , ")
        newrow.index=index
        newrow.qty_ord=qty_ord
        newrow.qty_ship=qty_ship
        newrow.part=part
        newrow.m_part=m_part
        newrow.price=price
        newrow.extended=extended
        return newrow


class Loader:
    def __init__(self,data_file):
        self.data_file_name = data_file

    def __repr__(self):
        return "Loader(%s)" % (self.data_file_name)

    def load_file(self):
        """ load_file opens the file and reads all rows, and loads rows into a list called rows """
        self.rows = []
        """ create the first row of dat from a bunch of text strings - making a header """
        self.rows.append(Row.row_from_columns("index","qty_ord","qty_ship","part","m_part","price","extended"))
        
        self.file = open(self.data_file_name, "r")
        print(self.file)
        #print (self.file.readline() ) 

        for line in self.file: 
            print (line)
            self.rows.append(Row(line))

    def get_rows(self):
         for row in self.rows: 
            print (row)
            



#mainline program
try:
    file_loader = Loader("electronics.csv")
    print (file_loader)
    file_loader.load_file()
    file_loader.get_rows

except FileNotFoundError as fnf_error:
    print("mega Fail")
    print(fnf_error)


print( "done")