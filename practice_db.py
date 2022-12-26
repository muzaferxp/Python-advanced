import sqlite3


def runQry(qry):
    #step 1. CREATE/ CONNECT DATABASE
    con = sqlite3.connect("practice.db")
    cur = con.cursor()

    #step 2. Execute query
    cur.execute(qry)

    #step 3. Print the data
    if "select" in qry.lower():
        for x in cur.fetchall():
            print(x)
    else:
        con.commit()
    print("Query executed successfully")
    con.close()




#2. Create A Table
# runQry("CREATE TABLE notification (id, title, description, time)")


#3. INSERT (add Data)
# runQry("INSERT INTO notification values(1, 'Notification title', 'NOtification desc', '16:30')")


#4. SELECT  (reading the data)
# runQry("SELECT * from user")

#5. Where claus
# runQry("SELECT * from user WHERE id='3' or id='2' ")

#6. UPDATE 
# runQry("UPDATE user set phone='7799399907' where name='Musaddiq'")

#7. DELETE  (delete a single record)
# runQry("DELETE from user_backup WHERE name='Notification title'")

#8. TRUNCATE  (delete all records)
# runQry("DELETE FROM notification")

#9.  DROP
# runQry("DROP table notification")

#10. Create a backup of table
# runQry("CREATE TABLE user_backup as select * from user")


#11. ALTER a table  (UPDATE )
# runQry("ALTER TABLE user add column email")


#FINALLY SQL VS NO SQL
