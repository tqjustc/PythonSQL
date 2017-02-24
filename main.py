import os, sys
# I put setting parameters into the ../setting.py,
# which includes SERVERIP, USERNAME, PASSWORD, DBname
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from setting import *

import MySQLdb
import pdb
pdb.set_trace()
conn = MySQLdb.connect(serverIP, username, password, DBname)
cursor = conn.cursor()
cursor.execute("""
	SELECT TABLE_NAME FROM information_schema.tables
	WHERE TABLE_TYPE='BASE TABLE'
""")

row = cursor.fetchone()
while row:
	print row
	row = cursor.fetchone()
# the above codes print all tables' names in the database (DBname)

#################
# query all information in this table 'admin_messages' 
#################
pdb.set_trace()
sql_cmd = """
SELECT * FROM admin_messages;
"""
cursor = conn.cursor()
cursor.execute(sql_cmd)
row = cursor.fetchone()
while row:
        print row
        row = cursor.fetchone()
	
conn.close()

print 'Program Ends.'
