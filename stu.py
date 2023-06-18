import sqlite3
con=sqlite3.connect('student.db')
def insertData(name,age,dep):
    qry="insert into student(NAME,AGE,DEP)values(?,?,?)"
    con.execute(qry,(name,age,dep))
    con.commit()
    print("user details added")
def updateData(name,age,dep,id):
    qry="update student set NAME=?,AGE=?,DEP=?,where id=?;"
    con.execute(qry,(name,age,dep,id))
    con.commit()
    print("user details update")
def deleteData(id):
    qry="delete from student where id=?;"
    con.execute(qry(id))
    con.commit()
    print("user details deleted")
def selectData():
    qry="select*from student"
    result=con.execute(qry)
    for row in result:
        print("row")
print("""
1. Insert
2. Update
3.Delete
4.Select
""")
ch=1
while ch==1:
    c=int(input("select your choice:"))
    if(c==1):
        print("add new record")
        name=input("enter name:")
        age=input("enter age:")
        dep=input("enter dep:")
        insertData(name,age,dep)
    elif(c==2):
        print("edit a record")
        id=input("enter ID:")
        name=input("enter name:")
        age=input("enter age:")
        dep=input("enter dep:")
        updateData(name,age,dep,id)
    elif(c==3):
        print("delete a record")
        id=input("enter id:")
        deleteData(id)
    elif(c==4):
        print("print all record")
        selectData()
    else:
        print("ivalid selection")
ch=int(input("enter 1 to continue:"))
print("thank you")
