#!/usr/bin/python

#
# this is the interface by which the JavaScript interacts with the "back-end"
# (database, persistent storage) of the rest of the system
#
# the JS makes get/post requests to this CGI, and this prints data (initially
# in CSV format) which the JS parses and presents to the user (via HTML or
# high charts, etc.)
#

import os
import cgi
import DbSqlite

if ('HTTP_HOST' in os.environ) and (os.environ['HTTP_HOST'] == 'localhost'):
    import cgitb
    cgitb.enable()

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------

print "Content-Type: text/html\x0d\x0a\x0d\x0a",

db    = DbSqlite.DbSqlite('yarms.db')
form  = cgi.FieldStorage()

# Read in the request type...
op = ''
if 'op' in form:
    op = form['op'].value

# Commands received via cgi
if op == 'getEmployeeNames':        db.getEmployeeNames()
if op == 'getEmployeeInfoByName':   db.getEmployeeInfoByName(form['name'].value)
if op == 'getEmployeeInfoByKey':    db.getEmployeeInfoByKey(form['key'].value)
if op == 'getFeedbackQuestions':    db.getFeedbackQuestions()
if op == 'submitFeedback':          db.submitFeedback(form['target_key'].value,form['provider_key'].value,form['category_key'].value,form['comment'].value)

if op == 'genEmployeeReportByName': db.genEmployeeReportByName(form['name'].value)
