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
    
    def genEmployeeReportByName(self,name):                
        self.c.execute('SELECT key,id,title,supervisor_key from employees where name=?', (name,))
        t_result = self.c.fetchone()
        target_key  = t_result[0]
        t_id        = t_result[1]
        t_title     = t_result[2]
        t_super_key = t_result[3]        
        self.c.execute('SELECT name from employees where key=?', (t_super_key,))  
        t_super = self.c.fetchone()[0]        
        self.c.execute('select feedback.date, employees.name, comments.comment from feedback,comments,employees where feedback.target_key = ' + str(target_key) + ' and feedback.comment_key = comments.key and feedback.provider_key = employees.key;')
        report = '=' * 80 + '\n'
        report += 'Employee Report:\n'
        report += '       Name: ' + name + '\n'
        report += '     Emp ID: ' + t_id + '\n'
        report += '      Title: ' + t_title + '\n'
        report += ' Supervisor: ' + t_super + '\n'
        report += '=' * 80 + '\n'
        for x in self.c.fetchall():
            report += x[0][0:10] + '\t' + x[1] + '\t' + x[2] + '\n'
        report = report[:-1] 
        print report
    
    
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

