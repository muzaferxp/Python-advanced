from flask import * 
import core
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)


#1st API 
@app.route("/members")
@cross_origin()
def members():
    return {
        "data" : core.getAllMembers()
    }
    
#2nd API 
@app.route("/members/<phone>")
def membersByNumber(phone):
    return {   
     "data" : core.getMemberByPhoneNumber(phone)
     }


#3rd API
@app.route("/create-member", methods=["POST"])
def createMember():
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']

    core.createMember({
        "name" : name,
        "email" : email,
        "phone" : phone
    })
    return "Member created successfully"



#3rd API
@app.route("/update-member", methods=["PUT"])
def updateMember():
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']

    core.updateMember(phone, {
        "name" : name,
        "email" : email,
        "phone" : phone
    })
    return "Member updated successfully"
    
@app.route("/delete-member/<phone>", methods=["DELETE"])
def deleteMember(phone):
    core.deleteMember(phone)
    return "Member deleted successfully"
    

if __name__ == "__main__":
    app.run()