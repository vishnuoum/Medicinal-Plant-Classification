from flask import Blueprint, request, Response
import repository
from logConfig import logging
import json
from datetime import datetime
import util
import os
from scraper import nearBy



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

    # call login function in repository file by passing phone and pasword as parameters and return unique user id
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

    # call signup function in repository by passing username, phone and password and return unique user id
    result=repository.signup(name=request.form.get("username"),phone=request.form.get("phone"), password = request.form.get("password"))
    if(result == "exists"):
        return Response(response="Exists",status=200)
    if(result!="error"):
        logging.info("-----Signup success-----\n")
        return Response(json.dumps(result),status=200,content_type="application/json")
    else:
        logging.info("-----Signup failure-----\n")
        return Response(response="Error",status=401)
    

# getUsername
@controller.post("/getUsername")
def getUsername():
    logging.info("-----Hit Get username End point-----\n")
    logging.info("Request Parameters %s",request.form)

    # calling get username function in repository file to get the username of corresponding user id
    result=repository.getUsername(id=request.form.get("id"))
    if(result!="error"):
        logging.info("-----Get username success-----\n")
        return Response(json.dumps(result),status=200,content_type="application/json")
    else:
        logging.info("-----Get username failure-----\n")
        return Response(response="Error",status=401)


# getPlants route
@controller.get("/getPlants")
def getPlants():

    # calling getPlants function in repository to list of plants
    result=repository.getPlants(q=request.args.get("q").strip())
    if(result!="error"):
        logging.info("-----Getting plant list-----\n")
        return Response(json.dumps(result),status=200,content_type="application/json")
    else:
        logging.info("-----Getting plant list failure-----\n")
        return Response(response="Error",status=400)


# getPurpose route
@controller.get("/getPurpose")
def getPurpose():

    # calling the getPurpose function in repository to get the benefits of plant with corresponding id
    result=repository.getPurpose(request.args.get("id"))
    print(result)
    if(result!="error"):
        logging.info("-----Getting purpose for plantid = %s-----\n",request.args.get("id"))
        return Response(json.dumps(result),status=200,content_type="application/json")
    else:
        logging.info("-----Getting plant list failure-----\n")
        return Response(response="Error",status=400)


# classify route
@controller.post("/classify")
def classify():
    # checking if image is available in the request
    if 'pic' not in request.files:
        return Response(response="Error",status=400)
    
    # getting current timestamp for storing the image
    now=datetime.now()

    # storing the image in uploads folder
    file1 = request.files['pic']
    path = os.path.join('./uploads', now.strftime("%d%m%Y%H%M%S")+file1.filename)
    file1.save(path)

    # classifying the image
    result=util.classify(path)
    if(result=="error"):
        return Response(response="Error",status=400)
    elif(result=="Not satisfied"):
        return Response(response="No Leaf",status=400)
    return Response(response=json.dumps(result, default=str),status=200)

@controller.get("/nearby")
def nearby():

    # calling get nearby function
    result = nearBy(location=request.args.get("location"))
    if(result == "error"):
        return Response(response="Error",status=400)
    else:
        return Response(response=json.dumps(result, default=str),status=200)