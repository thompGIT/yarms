#------------------------------------------------------------------------------
# DbSqlite.py
#------------------------------------------------------------------------------

import sqlite3
import string
import time
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
                
    def getELevel(self,employee):
        self.c.execute('SELECT title from employees where name=?', (name,))
        print self.c.fetchone()[0]        
    
    #--------------------------------------------------------------------------
    # setup
    #--------------------------------------------------------------------------
    def __init__(self, path):

#        print 'Attaching to database at [' + path + ']'

        # Connect to the database (assumes it already exists!)
        if ( os.path.exists(path) ):
            self.conn = sqlite3.connect(path)
            self.c = self.conn.cursor()
        else:
            print 'ERROR: Unable to locate database!'
            sys.exit(1)

