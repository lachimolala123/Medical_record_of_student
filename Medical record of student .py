import mysql.connector as sql

def user_input(entry, data_type=str):
    while True:
        try:
            user_input = data_type(input(entry))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def create_connection():
    return sql.connect(host='localhost', user='root', passwd='Aacpr2385%', database='MedRep')

'''def create_table():
    conn = create_connection()
    cr = conn.cursor()
    cr.execute(
        "create table if not exists users ("
        "AdminNo int primary key, "
        "Sname varchar(25) not null"
        ");"
    )
    cr.execute(
        "create table if not exists records ("
        "AdminNo int primary key, "
        "Sname varchar(25) not null, "
        "Sex char(10) not null, "
        "Mname varchar(20), "
        "Fname varchar(20), "
        "Age int not null, "
        "ClassSec varchar(10) not null, "
        "DoB date not null, "
        "BloodGroup varchar(4) not null, "
        "Height float, "
        "Weight float, "
        "Allergies varchar(100), "
        "Tetanus char(1), "
        "Cholera char(1), "
        "Typhoid char(1), "
        "HepA char(1), "
        "HepB char(1), "
        "ChickenPox char(1), "
        "Measles char(1), "
        "COVID char(1), "
        "AnyOther varchar(20)"
        ");"
    )
    conn.commit()
    conn.close()'''

def sign_up():
    print('\n- - -PERSONAL DETAILS- - -\n')
    admin_no = user_input("Enter Admin No.: ", int)
    s_name = user_input("Enter Student Name: ")
    sex = user_input("Enter Sex (M/F): ")
    mother_name = user_input("Enter Mother's Name: ")
    father_name = user_input("Enter Father's Name: ")
    age = user_input("Enter Age: ", int)
    class_sec = user_input("Enter Class & Sec: ")
    dob = user_input("Enter Date of Birth [YYYY-MM-DD]: ", str)
    bgrp = user_input("Enter Blood Group: ")
    print('\n- - -PHYSICAL RECORDS- - -\n')
    height = user_input("Enter Height (cm): ", float)
    weight = user_input("Enter Weight (kg): ", float)
    allergies = user_input("Enter Allergies: ")
    print('\n- - -VACCINATIONS- - -\n')
    tetanus = user_input("Tetanus Vaccinated? (Y/N): ").upper()
    cholera = user_input("Cholera Vaccinated? (Y/N): ").upper()
    typhoid = user_input("Typhoid Vaccinated? (Y/N): ").upper()
    hep_a = user_input("Hepatitis A Vaccinated? (Y/N): ").upper()
    hep_b = user_input("Hepatitis B Vaccinated? (Y/N): ").upper()
    chicken_pox = user_input("Chickenpox Vaccinated? (Y/N): ").upper()
    measles = user_input("Measles Vaccinated? (Y/N): ").upper()
    covid = user_input("COVID Vaccinated? (Y/N): ").upper()
    any_other = user_input("Any Other Information: ")
    print('\n\nRecords successfully added!')
    conn = create_connection()
    cr = conn.cursor()
    cr.execute("INSERT INTO users (AdminNo, Sname) VALUES ({}, '{}')".format(admin_no, s_name))
    insert_query="""insert into records(AdminNo,Sname,Sex,Mname,Fname,Age,ClassSec,DoB,
                    BloodGroup,Height,Weight,Allergies,Tetanus,Cholera,Typhoid,HepA,HepB,
                    ChickenPox,Measles,COVID,AnyOther)
                    values({},'{}','{}','{}','{}',{},'{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
                """.format(admin_no,s_name,sex,mother_name,father_name,age,class_sec,dob,
                        bgrp,height,weight,allergies,tetanus,cholera,typhoid,hep_a,hep_b,
                        chicken_pox,measles,covid,any_other)
                                                           
    cr.execute(insert_query)
    conn.commit()
    conn.close()

def adminsign_in():
    print("\nSigning in as Administrator\n")
    admin_name = user_input("Administrator name: ")
    admin_pass = user_input("Administrator password: ")
    if admin_name == "GOD#01" and admin_pass == "Alpha58296%":
        print("A one-time password (OTP) has been sent to your registered device.")
        admin_otp=user_input("Enter OTP: ")
        if admin_otp == "0001":
            print("Administrator sign-in successful.")
            admin_dash()
        else:
            print("Administrator sign-in failed.\nInvalid OTP.")
    else:
        print("Administrator sign-in failed.\nInvalid credentials.")
        
#ADMIN VIEW CHOICE
        
def admin_dashview():
    admit_no=int(input("Enter the Admin no.:"))
    s_name=input('Enter Student name:')
    conn=create_connection()
    cr=conn.cursor()
    cr.execute("select*from records where AdminNo={} and Sname='{}'".format(admit_no,s_name))
    records = cr.fetchone()
    print("\nStudent Records:")
    print("Admin No.: {}".format(records[0]))
    print("Student Name: {}".format(records[1]))
    print("Sex: {}".format(records[2]))
    print("Mother's Name: {}".format(records[3]))
    print("Father's Name: {}".format(records[4]))
    print("Age: {}".format(records[5]))
    print("Class & Sec: {}".format(records[6]))
    print("Date of Birth: {}".format(records[7]))
    print("Blood Group: {}".format(records[8]))
    print("Height: {}".format(records[9]))
    print("Weight: {}".format(records[10]))
    print("Allergies: {}".format(records[11]))
    

#ADMIN SORT CHOICE
        
def bloodgroup():
    bg=input('Enter the blood group').upper()
    a=['A+','B+','O+','AB+','A-','B-','AB-','O-']

    if bg not in a:
       print('Please enter the correct blood group')
    else:
        conn=create_connection()
        cr=conn.cursor()
        cr.execute("select Sname from records where BloodGroup='{}'".format(bg))
        data=cr.fetchall()
        for i in data:
            print(i)
        
def nummfsec():
    class_sec=input('Enter class and section').upper()
    a=['I-A','I-B','I-C','II-A','II-B','II-C','III-A','III-B','III-C','IV-A','IV-B','IV-C','V-A','V-B',
       'V-C','VI-A','VI-B','VI-C','VII-A','VII-B','VII-C','VIII-A','VIII-B','VIII-C','IX-A','IX-B','IX-C','X-A',
       'X-B','X-C','XI-A','XI-B','XI-C','XI-D','XII-A','XII-B','XII-C','XII-D','KGA','KGB',
       'KGC','NRA','NRB','NRC']
    if class_sec not in a:
        print('Please enter the correct class and section')
    else:
        conn=create_connection()
        cr=conn.cursor()
        cr.execute("select count(Sex) from records where ClassSec='{}'and Sex='M'".format(class_sec))
        data=cr.fetchall()
        for i in data:
            print('Number of Male are')
            print(i)
        cr.execute("select count(Sex) from records where ClassSec='{}'and Sex='F'".format(class_sec))
        data=cr.fetchall()
        for i in data:
            print('Number of Female are')
            print(i)
            
def nummfsc():
    conn=create_connection()
    cr=conn.cursor()
    cr.execute("select count(Sex) from records where Sex='M'")
    data=cr.fetchall()
    print('Number of Males in school are')
    for i in data:
        print(i)
    cr.execute("select count(Sex) from records where Sex='F'")
    data=cr.fetchall()
    print('Number of Females in school are')
    for i in data:
        print(i)
        
def tet():
    conn=create_connection()
    cr=conn.cursor()
    cr.execute("select Sname,ClassSec from records where Tetanus='Y'")
    data=cr.fetchall()
    print('Who are vaccinated')
    for i in data:
        print(i)
    cr.execute("select Sname,ClassSec from records where Tetanus='N'")
    data=cr.fetchall()
    print('Who are not vaccinated')
    for i in data:
        print(i)

def Cho():
    conn=create_connection()
    cr=conn.cursor()
    cr.execute("select Sname,ClassSec from records where Cholera='Y'")
    data=cr.fetchall()
    print('Who are vaccinated')
    for i in data:
        print(i)
    cr.execute("select Sname,ClassSec from records where Cholera='N'")
    data=cr.fetchall()
    print('Who are not vaccinated')
    for i in data:
        print(i)
        
def typ():
    conn=create_connection()
    cr=conn.cursor()
    cr.execute("select Sname,ClassSec from records where Typhoid='Y'")
    data=cr.fetchall()
    print('Who are vaccinated')
    for i in data:
        print(i)
    cr.execute("select Sname,ClassSec from records where Typhoid='N'")
    data=cr.fetchall()
    print('Who are not vaccinated')
    for i in data:
        print(i)

def hepa():
    conn=create_connection()
    cr=conn.cursor()
    cr.execute("select Sname,ClassSec from records where HepA='Y'")
    data=cr.fetchall()
    print('Who are vaccinated')
    for i in data:
        print(i)
    cr.execute("select Sname,ClassSec from records where HepA='N'")
    data=cr.fetchall()
    print('Who are not vaccinated')
    for i in data:
        print(i)

def hepb():
    conn=create_connection()
    cr=conn.cursor()
    cr.execute("select Sname,ClassSec from records where HepB='Y'")
    data=cr.fetchall()
    print('Who are vaccinated')
    for i in data:
        print(i)
    cr.execute("select Sname,ClassSec from records where HepB='N'")
    data=cr.fetchall()
    print('Who are not vaccinated')
    for i in data:
        print(i)
        
def chick():
    conn=create_connection()
    cr=conn.cursor()
    cr.execute("select Sname,ClassSec from records where ChickenPox='Y'")
    data=cr.fetchall()
    print('Who are vaccinated')
    for i in data:
        print(i)
    cr.execute("select Sname,ClassSec from records where ChickenPox='N'")
    data=cr.fetchall()
    print('Who are not vaccinated')
    for i in data:
        print(i)

def meas():
    conn=create_connection()
    cr=conn.cursor()
    cr.execute("select Sname,ClassSec from records where Measles='Y'")
    data=cr.fetchall()
    print('Who are vaccinated')
    for i in data:
        print(i)
    cr.execute("select Sname,ClassSec from records where Measles='N'")
    data=cr.fetchall()
    print('Who are not vaccinated')
    for i in data:
        print(i)
        
def covid():
    conn=create_connection()
    cr=conn.cursor()
    cr.execute("select Sname,ClassSec from records where COVID='Y'")
    data=cr.fetchall()
    print('Who are vaccinated')
    for i in data:
        print(i)
    cr.execute("select Sname,ClassSec from records where COVID='N'")
    data=cr.fetchall()
    print('Who are not vaccinated')
    for i in data:
        print(i)
    

                
def admin_dashsort():
    while True:
        
        print("1.Blood group wise breakup of the students.")
        print("2.Number of male and female students of a specific class and section.")
        print("3.Number of male and female in school")
        print("4.List of students who/who are not vaccination for Tetanus")
        print("5.List of students who/who are not vaccination for Cholera")
        print("6.List of students who/who are not vaccination for Typhoid")
        print("7.List of students who/who are not vaccination for Hepatitis A")
        print("8.List of students who/who are not vaccination for Hepatitis B")
        print("9.List of students who/who are not vaccination for Chicken pox")
        print("10.List of students who/who are not vaccination for Measles")
        print("11.List of students who/who are not vaccination for COVID")
        print("12.Exit")
        choice=int(input("Enter your choice :"))
        if choice==1:
            bloodgroup()
        elif choice==2:
            nummfsec()
        elif choice==3:
            nummfsc()
        elif choice==4:
            tet()
        elif choice==5:
            Cho()
        elif choice==6:
            typ()
        elif choice==7:
            hepa()
        elif choice==8:
            hepb()
        elif choice==9:
            chick()
        elif choice==10:
            meas()
        elif choice==11:
            covid()
        elif choice==12:
            print('Exiting..')
            break
        else:
            print('Enter the correct choice')
        
#ADMIN UPDATE CHOICE
        
def modify_name():
    a=int(input('Enter the admission number of the student'))
    conn=create_connection()
    cr=conn.cursor()
    cr.execute("select AdminNO from records")
    d=cr.fetchall()
    for i in d:
        if a in i:
            nam_old=input('Enter the old name of the student')
            nam_new=input('Enter the new name of the student')
            st="update records set Sname='{}' where Sname='{}' and AdminNo={}".format(nam_new,nam_old,a)
            cr.execute(st)
            print('Modified')
            break
        else:
            print('Wrong admission munber try again')
        
    conn.commit()
    
    
def modify_mname():
    a=int(input('Enter the admission number of the student'))
    conn=create_connection()
    cr=conn.cursor()
    cr.execute("select AdminNo from records")
    d=cr.fetchall()
    for i in d:
        if a in i:
            nam_old=input('Enter the old name of the mother')
            nam_new=input('Enter the new name of the mother')
            st="update records set Mname='{}' where Mname='{}' and AdminNo={}".format(nam_new,nam_old,a)
            cr.execute(st)
            print('Modified!')
            break
        else:
            print('Wrong admission number try again')
            
            
        
    conn.commit()
    

def modify_fname():
    a=int(input('Enter the admission number of the student'))
    conn=create_connection()
    cr=conn.cursor()
    cr.execute("select AdminNo from records")
    d=cr.fetchall()
    for i in d:
        if a in i:
           nam_old=input('Enter the old name of the father')
           nam_new=input('Enter the new name of the father')
           st="update records set Fname='{}' where Fname='{}' and AdminNo={}".format(nam_new,nam_old,a)
           cr.execute(st)
           print('Modified')
           break
            
            

        else:
           print('Wrong admission number')
           break

    conn.commit()
        
    
def modify_bdgp():
    a=int(input('Enter the admission number of the student'))
    conn=create_connection()
    cr=conn.cursor()
    cr.execute('select AdminNo from records')
    d=cr.fetchall()
    for i in d:
        if a in i:
             nam_old=input('Enter the old blood group')
             nam_new=input('Enter the new blood group')
             st="update records set BloodGroup='{}' where BloodGroup='{}' and AdminNo={}".format(nam_new,nam_old,a)
             cr.execute(st)
             print('Modified')
             break
             
        else:
            print('Wrong admission number try again')
            break
            
   
    conn.commit()
    
    
def modify_age():
    a=int(input('Enter the admission number of the student'))
    conn=create_connection()
    cr=conn.cursor()
    cr.execute('select AdminNo from records')
    d=cr.fetchall()
    for i in d:
        if a in i:
            nam_old=input('Enter the old age')
            nam_new=input('Enter the new age')
            st="update records set Age={} where Age={} and AdminNo={}".format(nam_new,nam_old,a)
            cr.execute(st)
            print('Modified!')
            break
        else:
            print('wrong admission number try again')
            break

    conn.commit()
            
            
    
    

    
    
    
    
        
def admin_update():
    while True:
        
        print('What do you want to edit?')
        print("1.Name")
        print("2.Mother's name")
        print("3.Father's name")
        print("4.Blood group")
        print("5.Age")
        print("6.Exit")
        choice=int(input('Enter the choice'))
        if choice==1:
            modify_name()
        elif choice==2:
            modify_mname()
        elif choice==3:
            modify_fname()
        elif choice==4:
            modify_bdgp()
        elif choice==5:
            modify_age()
        elif choice==6:
            print('Exiting...')
            break
            
        else:
            print('Please enter the correct choice')

        
    
    
#ADMIN DELETE CHOICE
    
def admin_delete():
    a=int(input('Enter the admission number to delete the record of the student'))
    conn=create_connection()
    cr=conn.cursor()
    cr.execute('select AdminNo from records')
    d=cr.fetchall()
    for i in d:
       if a in i:
            cr.execute("Delete from records where AdminNo={}".format(a))
            print('Deleted successfully!')
            break
       else:
            print('Wrong admission number try again')
            break
        
        
     
    
    conn.commit()
    
    
    
              
        
#ADMINS DASHBOARD
    
def admin_dash():
    
    while True:

     print("\nAdmin Dashboard")
     print("1. View User Records")
     print("2. Add User Record")
     print("3. Sort User Records")
     print("4. Update User Record")
     print("5. Delete User Record")
     print("6. Exit")
     choice=int(input("Enter your choice :"))
     if choice==1:
         admin_dashview()
     elif choice==2:
         sign_up()
     elif choice==3:
         admin_dashsort()
     elif choice==4:
         admin_update()
     elif choice==5:
         admin_delete()
     elif choice==6:
         print('Exiting..')
         break
         
     else:
         print("Invalid choice. Please try again.")

    


#USER DASHBOARD
         
def losersign_in():
    print("\nSigning in as Student")
    admit_no = user_input("\nEnter Admin No.: ", int)
    s_name = user_input("Enter Student Name: ")
    
    conn = create_connection()
    cr = conn.cursor()
    cr.execute("select * from users where AdminNo={} and Sname='{}'".format(admit_no, s_name))
    result = cr.fetchone()
    
    if result:
        print("Sign-in successful.\n")
        
        while True:
            print("\nWhat would you like to do?")
            print("1. View your records")
            print("2. Exit")
            choice = user_input("Enter your choice: ", int)
            
            if choice == 1:
                cr.execute("select * from records where AdminNo={} and Sname='{}'".format(admit_no, s_name))
                records = cr.fetchone()
                print("\nStudent Records:")
                print("Admin No.: {}".format(records[0]))
                print("Student Name: {}".format(records[1]))
                print("Sex: {}".format(records[2]))
                print("Mother's Name: {}".format(records[3]))
                print("Father's Name: {}".format(records[4]))
                print("Age: {}".format(records[5]))
                print("Class & Sec: {}".format(records[6]))
                print("Date of Birth: {}".format(records[7]))
                print("Blood Group: {}".format(records[8]))
                print("Height: {}".format(records[9]))
                print("Weight: {}".format(records[10]))
                print("Allergies: {}".format(records[11]))
            elif choice == 2:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    else:
        print("Invalid credentials. Sign-in failed.")

    cr.close()
    conn.close()

print("\t\tWelcome to the Student Medical Record Management System!\t\t")
'create_table()'
while True:
    print("\n1. Sign up")
    print("2. Sign in")
    print("3. Exit")
    choice = user_input("Enter your choice: ", int)

    if choice == 1:
        sign_up()
    elif choice == 2:
        sign_user=user_input("\n1. Sign in as Student\n2. Sign in as Administrator\n3. Exit\nEnter your choice: ", int)
        if sign_user==1:
            losersign_in()
        elif sign_user==2:
            adminsign_in()
        elif sign_user==3:
            print("Returning to main menu . . .")
            continue
        else:
            print("Error")
    elif choice == 3:
        print("Exiting...\n")
        break
    else:
        print("Invalid choice. Please try again.")
