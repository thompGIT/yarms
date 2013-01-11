#------------------------------------------------------------------------------
# DbSqlite.py
# Bugrack database module that uses SQLite for storage.
#------------------------------------------------------------------------------

import sqlite3
import string
import time
import os

class DbSqlite():

    #--------------------------------------------------------------------------
    # setup
    #--------------------------------------------------------------------------
    def __init__(self, path):

        # Connect to the database (assumes it already exists!)
        if ( os.path.exists(path) ):
            self.conn = sqlite3.connect(path)
            self.c = self.conn.cursor()
