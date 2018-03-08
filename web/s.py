import sqlite3

db = sqlite3.connect("db.sqlite3")
c = db.cursor()

sql = "create table Beacon(user_id,hw_id,time)"
c.execute(sql)

db.commit()
db.close()
