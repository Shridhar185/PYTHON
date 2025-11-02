
import sqlite3
from contextlib import closing   #automatically close the cursor object

def dbconnect():
    conn = sqlite3.connect("tw4.db")  #close dbbrowser before connect
    if conn:
        print("dbconnect success")
    else:
        print("dbconnect failure")
    return conn

def createtable(conn):
    with closing(conn.cursor()) as c:
        query='''create table if not exists products(p_id int,p_name text,quantity int,price real)'''
        c.execute(query)

def inserttable(conn):
    n=int(input("enter no of products: "))
    with closing(conn.cursor()) as c:
        for i in range(n):
            id1,name,quantity,price=input("enter id,name,quantity,price: ").split()
            id1=int(id1)
            quantity=int(quantity)
            price=float(price)
            query='''insert into products values(?,?,?,?)'''
            c.execute(query,(id1,name,quantity,price))
        conn.commit()

def dispall(conn):
    print("the products are: ")
    with closing(conn.cursor()) as c:        
        query='''select * from products'''
        c.execute(query)
        result=c.fetchall()
        #print("the products are: ",result)
        for prod in result:
            print(prod[0]," ",prod[1]," ",prod[2]," ",prod[3])

def delprod(conn):
    id1=int(input("enter product id which you delete: "))
    with closing(conn.cursor()) as c:       
        query='''delete from products where p_id=?'''
        c.execute(query,(id1,)) # line should have a comma after (id1) to pass it as a tuple to the execute function. beacuase execute expects a tuple as the second argument,
        print("after delete")
        dispall(conn)
    conn.commit()

def incrprice(conn):
    print("increasing price by 10%: ")
    #perc=float(input("enter how much percent increase price: "))
    with closing(conn.cursor()) as c:       
        query='''update products set price=price+price*0.1 where price < 50'''
        c.execute(query) 
        #query='''update products set price=price+price*?'''
        #c.execute(query,(perc,))  
        print("after updating")
        dispall(conn)
    conn.commit()

def dispbyquantity(conn):
    quant=int(input("display products below quantity: "))
    with closing(conn.cursor()) as c:
        query='''select * from products where quantity < ?'''
        c.execute(query,(quant,))
        result=c.fetchall()
        if len(result)>0:
            for prod in result:
                print(prod[0],prod[1],prod[2],prod[3])
        else:
            print("no products below that quantity\n")
         
def main():
    conn = dbconnect()
    createtable(conn)
    while(1):
        print("1.insert values \n2.display table\n3.delete product\n4.increase product price\n5.display by quantity\n6.exit")
        opt=int(input("enter the option "))
        if opt==1:
            inserttable(conn)
        elif opt==2:
            dispall(conn)
        elif opt==3:
            delprod(conn)
        elif opt==4:
            incrprice(conn)
        elif opt==5:
            dispbyquantity(conn)
        elif opt==6:
            break
        else:
            print("invalid option: ")

if __name__ == '__main__':
    main()

  