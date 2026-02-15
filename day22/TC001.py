import mysql.connector
host="localhost"
user="root"
password="root"
database="database"

conn=mysql.connector.connect(host=host,user=user,password=password,database=database)
cursor=conn.cursor()
print("connected to the database successfully")

query="SELECT * FROM database.employee"
#query="INSERT INTO `database`.`employee` (`employee id`, `employee name`) VALUES ('102', 'Sita');"

cursor.execute(query)

result=cursor.fetchall()

for row in result:
    print(row)