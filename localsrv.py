#!/usr/bin/python

import CGIHTTPServer
import BaseHTTPServer

# "Only directory-based CGI are used - the other common server configuration 
# is to treat special extensions as denoting CGI scripts."
class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
    cgi_directories = ["/cgi"]

PORT = 8080

httpd = BaseHTTPServer.HTTPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()

