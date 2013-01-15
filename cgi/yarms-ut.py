#!/usr/bin/python

#
# YARM Unit Test Helper
#

import sys
import random
import DbSqlite

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------

db = DbSqlite.DbSqlite('../yarms.db')
num_args = len(sys.argv)

if not ((num_args == 2) or (num_args == 3)): 
    print 'Usage: ' + str(sys.argv[0]) + ' <command> [parameter]'
    print ' Commands: genEmployees [count]'
    print '           getEmployeeNames'
    sys.exit(1)

if sys.argv[1] == 'getEmployeeNames':
    if num_args != 2:
        print 'Usage: ' + str(sys.argv[0]) 
        sys.exit(1)
    db.getEmployeeNames()

if sys.argv[1] == 'genEmployees':
    if num_args != 3:
        print 'Usage: ' + str(sys.argv[0]) + ' genEmployees [count]'
        sys.exit(1)

    num_employees = int(sys.argv[2])
    firstNames = ['James','John','Robert','Michael','William','David','Richard','Charles','Joseph','Thomas']
    middleNames = ['Deon','Josiah','Rico','Trey','Dewitt','Fritz','Milford','Jerold','Napoleon','Jamaal','Yong']
    lastNames = ['Smith','Johnson','Williams','Jones','Brown','Davis','Miller','Wilson','Moore','Taylor','Martin']

    print 'Removing old employees...'
    db.delAllEmployees()
    print 'Generating ' + str(num_employees) + ' employees...'
    for i in range(num_employees):
        name = random.choice(firstNames) + ' ' + random.choice(middleNames) + ' ' + random.choice(lastNames)
        empId = 'SIG-' + str(i)
        title = 'E0' + str(random.randint(1,6))
        supervisor = random.randint(1,num_employees-1) % 5
        print '[' + title + '] [' + empId + '] [' + str(supervisor) + '] ' + name
        db.addEmployee(name,empId,title,supervisor)
        


