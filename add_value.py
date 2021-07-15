name=input("Enter Name :")
dept=input("Dept :")
m1=int(input("m1 :"))
m2=int(input("m2 :"))
m3=int(input("m3 :"))
m4=int(input("m4 :"))
m5=int(input("m5 :"))

totalm= m1+m2+m3+m4+m5
avg= totalm/5
print(totalm)
print(avg)
if avg==100:
    grade="O"
    print("O")
elif avg<100 and avg>90:
    grade="A"
    print("A")
elif avg<90 and avg>80:
    grade="B"
    print("B")
elif avg<80 and avg>70:
    grade="C"
    print("C")
elif avg<70 and avg>60:
    grade="D"
    print("D")
elif avg<60 and avg>50:
    grade="E"
    print("E")
else:
    grade="F"
    print("F")

import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database= "guvi_data_science"

)

mycursor=mydb.cursor()
mycursor.execute("INSERT INTO students (name, dept, m1, m2, m3, m4, m5, totalm, avg, grade)"
   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(name,dept,m1,m2,m3,m4,m5,totalm,avg,grade))
mydb.commit()
