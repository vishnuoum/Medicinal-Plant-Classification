import pymysql


#db connect
hostname = 'localhost'
username = 'root'
password = ''
database = 'plant'
myconn = pymysql.connect( host=hostname, user=username, passwd=password, db=database ,cursorclass=pymysql.cursors.DictCursor)
conn = myconn.cursor()