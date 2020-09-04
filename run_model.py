from flask import Blueprint, jsonify, request
import pymongo
bp = Blueprint("run_model", __name__)
import constants as const

#----------------USER ROUTES----------------------#

@bp.route("/get_users", methods=["GET"])
@bp.route("/get_users/", methods=["GET"])
def get_users():
    coll = const.mydb.user
    user_list = []
    user_query = coll.find()
    if(user_query):
        for user in user_query:
            user["_id"]=str(user["_id"])
            if(user["address"]):
                user_list.append(user)
        status = 'Success'
    else:
        status = 'No Users Found'
    return jsonify({"status":status, "data": user_list})


@bp.route("/get_users/<address>",methods = ["GET"])
def get_user(address):
    coll = const.mydb.user
    user=coll.find_one({"address":address})
    result="No Data"
    print(user)
    if(user and user["_id"]!=None):
        status_response='Success'
        user["_id"]=str(user["_id"])
        result = user
    else:
        status_response='User Not Found'
    return jsonify({"status":status_response,"data":result})

@bp.route("/add_users",methods=["POST"])
def add_users():
    coll = const.mydb.user
    name = request.json["name"]
    image = request.json["image"]
    email = request.json["email"]
    address = request.json["address"]
    tagline = request.json["tagline"]

    if(coll.find_one({"address" :address})):
        return jsonify({"status": "Faliure, Address is in use","data":"No data"})

    obj={"name":name, "image":image, "email":email, "address":address, "tagline":tagline}
    status_response = coll.insert_one(obj)
    if (status_response):
            status_response="Success"
    else:
            status_response="Failure"
    response = jsonify({"status": status_response,"data":[]})
    return response

@bp.route("/delete_users",methods=["POST"])
def delete_users():
    address = request.json["address"]
    coll = const.mydb.user
    user = coll.find_one({"address":address})
    user["_id"]=str(user["_id"])
    if(user):
        status_response = coll.delete_one({"address":address})
        if(status_response):
            status_response="Success"
        else:
            status_response="Failure"
    else:
        status_response="Failure"
    return jsonify({"status":status_response,"data":user})

@bp.route("/update_users",methods=["POST"])
def update_user():
    
    coll = const.mydb.user

    if(coll.find_one({"address":request.json["address"]})):
        obj=request.json
        status_response = coll.update_one({"address":request.json["address"]},{"$set":obj})
        if(status_response):
            status_response="Success"
        else:
            status_response="User Not Found"
    else:
        status_response="Failure"
    return jsonify({"status":status_response,"data":[]})