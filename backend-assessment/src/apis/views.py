import logging
from flask import request
from flask import json
from flask import jsonify
from models.user import User
from services.user_service import *



logger = logging.getLogger("default")
def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask caffolding application"


def login():
    """
    TASKS: write the logic here to parse a json request
           and send the parsed parameters to the appropriate service.

           return a json response and an appropriate status code
    """
    data = request.get_json()
    username = data['username']
    password = data['password']
    a = UserService()
    is_authenticate = UserService.login_user(User,username,password)
    
    return is_authenticate

