import sqlite3
import os.path



data_path = os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data\Default")
files = os.listdir(data_path)
history_db = os.path.join(data_path,'history')

c= sqlite3.connect(history_db)
cursor=c.cursor()
select_statement= "SELECT urls.url,urls.Visit_count FROM urls,Visits WHERE urls.id=visits.url;"

cursor.execute(select_statement)

for row in cursor:
    print(row)




