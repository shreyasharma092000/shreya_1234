import mysql.connector as a
con=a.connect(host='localhost',user="root",password="root",database="marriage_portal_management")


def reg():
    n=input("Enter your username:")
    r=input("Enter your password:")
    data=(n,r)
    sql='insert into registration values(%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("USER REGISTERED SUCCESSFULLY")
    print("***************************************************")
    main()

def rem():
    c=input("Enter username:")
    r=input("Enter password:")
    data=c,r
    sql='delete from registration where Name=%s and password=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("REGISTRATION CANCELLED")
    print("***************************************************")
    main()

def logus():
    n=input("Enter name:")
    s=input("Enter password:")
    sql_sel="select*from login where password='"+str(s)+"'and name='"+n+"'"
    c=con.cursor()
    c.execute(sql_sel,)
    if c.fetchone() is None:
        print()
        print("ILLEGAL LOGIN,TRY AGAIN")
    else:
        print()
    print("***************************************************")
    main()

def bl():
    n=input("Enter your name:")
    s=input("Enter your age:")
    a=input("Enter your caste:")
    p=input("Enter your profession:")
    r=input("Enter your height_in_centimeters:")
    t=input("Enter your phone_no")
    data=(n,s,a,p,r,t)
    sql='insert into bride_details values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("BRIDE DETAILS ENTERED SUCCESSFULLY")
    print("**************************************************")
    main()

def delbd():
    j=input("Enter bride's name:")
    k=input("Enter phone_no:")
    data=j,k
    sql='delete from bride_details where name=%s and phone_no=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("DATA DELETED")
    print("***************************************************")
    main()


def gl():
    d=input("Enter your name:")
    e=input("Enter your age:")
    f=input("Enter your caste:")
    g=input("Enter your profession:")
    h=input("Enter your height_in_centimeters:")
    i=input("Enter your phone_number")
    data=(d,e,f,g,h,i)
    sql='insert into groom_details values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("GROOM DETAILS ENTERED SUCCESSFULLY")
    print("****************************************************")
    main()

def delgd():
    l=input("Enter groom's name:")
    m=input("Enter phone_no:")
    data=l,m
    sql='delete from groom_details where name=%s and phone_no=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("DATA DELETED")
    print("***************************************************")
    main()

def disbl():
    n=input("caste:")
    data=(n,)
    sql="select*from bride_details where caste=%s"
    c=con.cursor()
    c.execute(sql,data)
    d=c.fetchall()
    for i in d:
        print("NAME:",i[0])
        print("AGE:",i[1])
        print("CASTE:",i[2])
        print("PROFESSION:",i[3])
        print("HEIGHT_IN_CM:",i[4])
        print("PHONE_NO:",i[5])
        print("_____________________________")
    print("***************************************************")
    main()

def disgl():
    n=input("caste:")
    data=(n,)
    sql="select*from groom_details where caste=%s"
    c=con.cursor()
    c.execute(sql,data)
    d=c.fetchall()
    for i in d:
        print("NAME:",i[0])
        print("AGE:",i[1])
        print("CASTE:",i[2])
        print("PROFESSION:",i[3])
        print("HEIGHT_IN_CM:",i[4])
        print("PHONE_NO:",i[5])
        print("_____________________________")
    print("***************************************************")
    main()

def main():
    print("""                       WELCOME TO OUR MATRIMONIAL WEBSITE

            PLEASE CHOOSE TASK FROM THE FOLLOWING-


                1.REGISTER USER                                  6.ENTER GROOM DETAILS
                2.REMOVE USER                                    7.DELETE GROOM DETAILS
                3.LOGIN USER                                     8.DISPLAY BRIDE'S LIST
                4.ENTER BRIDE DETAILS                            9.DISPLAY GROOM'S LIST
                5.DELETE BRIDE DETAILS         
""")
    ch=input("Enter task number:")
    print("************************************************")
    if(ch=='1'):
        reg()
    elif(ch=='2'):
        rem()
    elif(ch=='3'):
        logus()
    elif(ch=='4'):
        bl()
    elif(ch=='5'):
        delbd()
    elif(ch=='6'):
        gl()
    elif(ch=='7'):
        delgd()
    elif(ch=='8'):
        disbl()
    elif(ch=='9'):
        disgl()
    else:
        print("wrong choice")
        main()
main()
        
    
        
        
        
              


    
    
    
    
