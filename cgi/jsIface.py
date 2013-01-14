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

db    = DbSqlite.DbSqlite('yarm.db')
form  = cgi.FieldStorage()

# Read in the request type...
op = ''
if 'op' in form:
    op = form['op'].value

if op == 'sampleCmd':  db.sampleCmd()