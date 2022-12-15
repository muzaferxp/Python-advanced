import sqlite3

#1. Create the database
# con = sqlite3.connect("database.db")
# cur = con.cursor()

#2.Create A Table
# cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
# con.commit()

#3. Insert a row
# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Fullstack adventure', 2012, 8.2),
#         ('BEUTIFUL sql', 1997, 7.5)
# """)
# con.commit()

#4. Read the data from a table
def getData():
    con = sqlite3.connect("project1/database.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM movie")
    data = res.fetchall()
    print(data)
    con.close()
    return data

#5. Upate row
#6. Upate a table

#7. Delte a row
#8. Delete a table

#9. Alter table (to add or remove the columns)


#10. Drop Table/Database (Delete the data along with the table)
#11.Trucate  (Deletes the data, but table will not be deleted )

#12. Where (to filter the result)

#FINALLY SQL VS NO SQL