#sqlite3 is an version 3 of sqlite
#blob datatype for bytes

#to check connected or not 
""" import sqlite3
conn=sqlite3.connect("py3.db")
conn.close()
if conn:                    # it checks if the conn variable is not None. Since you've assigned the connection object to conn earlier, it is not None, and the condition is considered True.
    print("connected")
else:
    print("not connected")
 """

""" 
import sqlite3
conn=sqlite3.connect("py.db")
conn.execute('''drop table student''') #to delete table 
conn.close()
 """




""" import sqlite3
conn=sqlite3.connect("py.db")
conn.row_factory=sqlite3.Row
#conn.execute('''create table student(s_id int primary key,s_name varchar(10),s_div varchar(2))''')

ins='''insert into student values(13,'karna','a')'''      #withot changing values if we run it gives error because id is primary key
conn.execute(ins)
conn.commit()                                              #it saves previously inserted values afte changing,new value inserted old values will still there

data=conn.execute("select * from student")
for n in data:
    print(n)                                      #give as a touples line by line
#for n in data:
#    print(n[0]," ",n[1]," ",n[2])
"""









import sqlite3
conn=sqlite3.connect("py.db")
#conn.row_factory=sqlite3.Row         #to access columns by name of column
c=conn.cursor()                       #getting a cursor from connection object
c.execute('''create table if not exists student(s_id int,s_name varchar(10),s_div varchar(2))''')
ins='''insert into student values(3,'arjuna','a')'''
c.execute(ins)
conn.commit()          #c.commit not possible because cursor object has no commit method,The commit() method is of connection object
c.execute("select * from student")
#print(c.fetchone())   #give first line 

print(c.fetchall())    #give each line as items in a list, except first line if above line present

#for li in c.fetchall():
#    print("name: ",li["s_name"])       #access by column name

""" #When conn.row_factory = sqlite3.Row is set, the result of print(c.fetchall()), it will display the rows as Row objects, which not readable.
rows = c.fetchall()
students = [dict(row) for row in rows]     # Convert rows to dictionaries for readability
print(students)
 """
conn.close()











""" 
#we can use if not exists in create table --->it executes table only if it not present 
import sqlite3
def createtable(conn):
    conn.execute('''create table if not exists student(s_id int primary key, s_name varchar(10), s_div varchar(2))''')
    print("table created")

def insert_student(conn):
    s_id = int(input("Enter student ID: "))
    s_name = input("Enter student name: ")
    s_div = input("Enter student division: ")

    #ins = f"insert into student values({s_id}, '{s_name}', '{s_div}')"
    #conn.execute(ins)
    ins = '''insert into student values (?, ?, ?)'''      #we can replace ''' by "
    conn.execute(ins, (s_id, s_name, s_div))
    conn.commit()

def display_students(conn):
    print("\nStudents in the database:")
    data = conn.execute("select * from student")
    for n in data:
        print(n[0], " ", n[1], " ", n[2])

def deletetable(conn):
    try:
        conn=sqlite3.connect("py.db")
        conn.execute('''drop table student''') #to delete table 
        conn.close()
    except:
        print("no such file")
     
def main():
    conn = sqlite3.connect("py.db")
    while(1):
        print("\n1.createtable\n2.insert values\n3.display students\n4.deletetable\n5.exit")
        opt=int(input("enter your option: "))
        if opt==1:
            createtable(conn)
        elif opt==2:
            insert_student(conn)
        elif opt==3:
            display_students(conn)      # Display all students
        elif opt==4:
            deletetable(conn)
        elif opt==5:
            break
        else:
            print("invalid options")

if __name__ == '__main__':
    main()
 
 """
 
 
 