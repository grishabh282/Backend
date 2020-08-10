import datetime
from app import celery
from flask import jsonify

@celery.task
def insertLastLoginTime(arg1):
    #
    current_login_time =   datetime.datetime.now
    arg[0].updtae(last_login=current_login_time)
    return True


class UserService(object):
    """
    service function for user related business logic
    """

    def login_user(*argv):
        """
        TASKS: write the logic here for user login
               authenticate user credentials as per your
               schema and return the identifier user.

               raise appropriate errors wherever necessary
        """
        user = argv[0]
        username = argv[1]
        password = argv[2]

        if username=='' and password=='':
            return jsonify(success ="username and password is required",status="2")
        if username:

            if password:

                all_user = user.objects(username=username,password=password)
                if all_user[0]:
                    res = insertLastLoginTime(all_user)
                    if res==True:
                        return jsonify(success = "{} logged in successfull".format(user),status="2")
                else:
                    return jsonify(success ="{} is not found".format(user),status="2")
            else:
                return jsonify(success ="password is required",status="2")
               
               
        else:
            return jsonify(success ="username is required",status="2")
               
        
            
