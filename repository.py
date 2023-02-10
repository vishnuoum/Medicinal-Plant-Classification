import pymysql
from logConfig import logging
import json
from dbConfig import conn , myconn


def login(phone, password):
    conn.execute("""Select sha2(id,256) as id from user where phone=%s and password=sha2(%s,256)""",[phone, password])
    logging.info("Execeuted Query ** %s **",conn._last_executed)
    result=conn.fetchone()
    logging.info("Login DB response = %s",json.dumps(result))
    if(result==None):
        return "error"
    else:
        return result

def signup(name, phone, password):
    if(conn.execute("""Insert into user(id, name, phone, password) values(NULL, %s, %s, sha2(%s,256))""",[name, phone, password])==True):
        logging.info("Execeuted Query ** %s **",conn._last_executed)
        myconn.commit()

        conn.execute("""Select sha2(%s,256) as id""",[myconn.insert_id()])
        result=conn.fetchone()
        logging.info("Login DB response = %s",json.dumps(result))
        return result
    else:
        logging.info("Data not inserted into DB")
        return "error"

def getPlants():
    conn.execute("""Select * from plant""")
    logging.info("Execeuted Query ** %s **",conn._last_executed)
    result=conn.fetchall()
    logging.info("Get Plants DB response = %s",json.dumps(result))
    if(result==None):
        return "error"
    else:
        return result

def getPurpose(id):
    conn.execute("""Select * from purposes where plantId=%s""",[id])
    logging.info("Execeuted Query ** %s **",conn._last_executed)
    result=conn.fetchall()
    logging.info("Get Purpose DB response = %s",json.dumps(result))
    if(result==None):
        return "error"
    else:
        return result