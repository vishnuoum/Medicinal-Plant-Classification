from flask import Blueprint, request, Response
import repository
from logConfig import logging
import json
from datetime import datetime
import util
import os



controller = Blueprint('controller',__name__)


# demo route
@controller.get("/")
def greet():
    return "Server is Up"


# login
@controller.post("/login")
def login():
    logging.info("-----Hit Login End point-----\n")
    logging.info("Request Parameters %s",request.form)

    result=repository.login(phone=request.form.get("phone"),password=request.form.get("password"))
    if(result!="error"):
        logging.info("-----Login success-----\n")
        return Response(json.dumps(result),status=200,content_type="application/json")
    else:
        logging.info("-----Login failure-----\n")
        return Response(response="Error",status=401)


# signup
@controller.post("/signup")
def signup():
    logging.info("-----Hit Singup End point-----\n")
    logging.info("Request Parameters %s",request.form)

    result=repository.signup(name=request.form.get("name"),phone=request.form.get("phone"), password = request.form.get("password"))
    if(result!="error"):
        logging.info("-----Signup success-----\n")
        return Response(json.dumps(result),status=200,content_type="application/json")
    else:
        logging.info("-----Signup failure-----\n")
        return Response(response="Error",status=401)


# getPlants route
@controller.get("/getPlants")
def getPlants():
    result=repository.getPlants()
    if(result!="error"):
        logging.info("-----Getting plant list-----\n")
        return Response(json.dumps(result),status=200,content_type="application/json")
    else:
        logging.info("-----Getting plant list failure-----\n")
        return Response(response="Error",status=400)


# getPurpose route
@controller.get("/getPurpose")
def getPurpose():
    result=repository.getPurpose(request.form.get("id"))
    if(result!="error"):
        logging.info("-----Getting purpose for plantid = %s-----\n",request.form.get("id"))
        return Response(json.dumps(result),status=200,content_type="application/json")
    else:
        logging.info("-----Getting plant list failure-----\n")
        return Response(response="Error",status=400)


# classify route
@controller.get("/classify")
def classify():
    if 'pic' not in request.files:
        return Response(response="Error",status=400)
    now=datetime.now()
    file1 = request.files['pic']
    path = os.path.join('./uploads', now.strftime("%d%m%Y%H%M%S")+file1.filename)
    file1.save(path)
    result=util.classify(path)
    if(result=="error"):
        return Response(response="Error",status=400)
    elif(result=="Not satisfied"):
        return Response(response="Could not find leaf",status=400)
    return Response(response=json.dumps(result, default=str),status=200)