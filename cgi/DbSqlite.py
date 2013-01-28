#------------------------------------------------------------------------------
# DbSqlite.py
#------------------------------------------------------------------------------

import sqlite3
import string
import time
import datetime
import os
import sys

class DbSqlite():

    def delAllEmployees(self):
        self.c.execute('DELETE FROM employees;')
        self.conn.commit()

    def addEmployee(self, name, empId, title, supervisor):
        self.c.execute('INSERT into employees (name,id,title,supervisor_key) VALUES (?,?,?,?)', (name,empId,title,supervisor))
        self.conn.commit()

    def getEmployeeNames(self):
        self.c.execute('SELECT name from employees order by name;')
        result = ''
        for x in self.c.fetchall():
            result += str(x[0]) + '\n'
        result = result[:-1]
        print result
                
    def getEmployeeInfoByName(self,name):
        self.c.execute('SELECT key,id,title,supervisor_key from employees where name=?', (name,))
        result = ''
        for x in self.c.fetchall():
            for i in range(len(x)):
                result += str(x[i]) + ','
        result = result[:-1]
        print result
                
    def getEmployeeInfoByKey(self,key):
        self.c.execute('SELECT name,id,title,supervisor_key from employees where key=?', (key,))        
        result = ''
        for x in self.c.fetchall():
            for i in range(len(x)):
                result += str(x[i]) + ','
        result = result[:-1]
        print result
                
    def getFeedbackQuestions(self):
        self.c.execute('SELECT key,text from categories;')        
        result = ''
        for x in self.c.fetchall():
            for i in range(len(x)):
                result += str(x[i]) + '`'
            result = result[:-1] + '\n'            
        if result != '':
            result = result[:-1]
        print result       
                
    def submitFeedback(self,target_key,provider_key,category_key,comment):    
        date = str(datetime.datetime.now())     
        self.c.execute('INSERT into comments (category_key,comment) VALUES (?,?);', (category_key,comment))
        self.c.execute('INSERT into feedback (date,provider_key,target_key,comment_key) VALUES (?,?,?,?);', (date,provider_key,target_key,self.c.lastrowid))
        self.conn.commit()
        
    
    #--------------------------------------------------------------------------
    # setup
    #--------------------------------------------------------------------------
    def __init__(self, path):

        # Connect to the database (assumes it already exists!)
        if ( os.path.exists(path) ):
            self.conn = sqlite3.connect(path)
            self.c = self.conn.cursor()
        else:
            print 'ERROR: Unable to locate database!'
            sys.exit(1)

