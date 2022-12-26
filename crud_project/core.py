import sqlite3


def runSqlQry(qry):
    data = []
    #1. Connecting to db file
    con = sqlite3.connect("members.db")
    
    #2. Initialize a cursor which is used to execute the sql query 
    cur = con.cursor()
    
    #3. Execute the query
    cur.execute(qry)
    
    if "select" in qry.lower():
        data = cur.fetchall()
    else:
        cur.execute("commit");
    
    con.close()
    
    return data        

def createMemberTable():
    runSqlQry("""
              CREATE TABLE member(
                name		varhcar(200),
                email		varhcar(200),
                phone		varhcar(200)
                );
              """)
    
# createMemberTable()

def createMember(details):
    runSqlQry(f"""
                INSERT INTO member values(
                    '{details['name']}',
                    '{details['email']}',
                    '{details['phone']}'
                )
              """)
    
# createMember({
#             "name" : "David",
#             "email"  : "david@123.in",
#             "phone" : "6549873210"
# })

def getAllMembers():
    data = runSqlQry("select * from member")
    print(data)
    return data

getAllMembers()

def getMemberByPhoneNumber(phoneNumber):
    data = runSqlQry(f"select * from member where phone ='{phoneNumber}' ")
    if len(data) == 0:
        print("Member not found")
    print(data)    
    return data
        
getMemberByPhoneNumber("9876543218")

def updateMember(phoneNumber, updatedDetails):
    runSqlQry(f"""UPDATE member set name='{updatedDetails['name']}' , 
                                    email = '{updatedDetails['email']}',
                                    phone = '{updatedDetails['phone']}'
                                    where phone='{phoneNumber}'
                                    """)

updateMember(
                "6549873210", 
                {
                    "name" : "David",
                    "email"  : "david@gmail.in",
                    "phone" : "1111111111"
                }
            )



def deleteMember(phoneNumber):
    runSqlQry(f"delete from member where phone = '{phoneNumber}'")
    
deleteMember("9876543218")
getAllMembers()
