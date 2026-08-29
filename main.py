import sqlite3
connect1=sqlite3.connect("full.db")
cursor1=connect1.cursor()
cursor1.execute("""CREATE TABLE IF NOT EXISTS users(
name TEXT,
grades TEXT,
grade TEXT)""")
connect1.commit()
def enter_number():
    print("enter number !")
def grade():
    print("not valid grade !")
def name():
    print("this name is already in list !")
def invalid_name():
    print("there is no name in the list")
def start():
    while True:
        try:
            menu=int(input("""school grade 7 to 9
            1. add student
            2. show student
            3. find student by name
            4. update students
            5. delete students
            6. exit
            type the number: """))
        except ValueError:
            enter_number()
        
        else:
            if menu==1:
                name1=input("gave your student name: ")
                try:
                    grade1=int(input("gave your student grade: "))
                except ValueError:
                    enter_number()
                else:

                    grade11=str(grade1)
                    if grade1>=7 and grade1<=9:
                        cursor1.execute(""" SELECT * FROM users WHERE name=?""",(name1,))
                        result1=cursor1.fetchone()
                        if result1 is None:
                            cursor1.execute("""INSERT INTO users (name, grade) VALUES(?,?)""",(name1,grade11,))
                            connect1.commit()
                           
                        else:
                            name()
                    else:
                        print("there is no grade like this !!!")
            elif menu==2:
                quest2=input("loking by grade type 1 and looking by all type 2: ")
                if quest2=="1":
                    try:
                        quest22=int(input("gave grade: "))
                    except ValueError:
                        enter_number()
                    else:
                        if quest22 in range(7,10):
                            q222=str(quest22)
                            cursor1.execute("""SELECT * FROM users WHERE grade=?""",(q222,))
                            result=cursor1.fetchall()
                            for rows in result:
                                print(f"name: {rows[0]} grades: {rows[1]} grade: {rows[2]}")
                elif quest2=="2":
                    cursor1.execute("SELECT name, grades,grade from users")
                    result11=cursor1.fetchall()
                    for things in result11:
                        print(f"name {things[0]} grades {things[1]} grade {things[2]}") 
                else:
                    print("there is something wrong !")
                    

            elif menu==3:
                name2=input("gave the student name: ")
                cursor1.execute("""SELECT * FROM users WHERE name=?""",(name2,))
                result2=cursor1.fetchone()
                if result2 is not None:
                    cursor1.execute("""SELECT name,grade FROM users WHERE name=?""",(name2,))
                    result22=cursor1.fetchone()
                    if result22 is not None:
                        print(f"name: {result22[0]} and age: {result22[1]}")
                else:
                    invalid_name()
            elif menu==4:
                name4=input("gave your name: ")
                cursor1.execute("SELECT * FROM users WHERE name=?",(name4,))
                result3=cursor1.fetchone()
                if result3 is None:
                    print("something is wrong")
                else:
                    quest=input("what do you want to change ? 1 for grades 2 for name, 3 for grade: ")
                    if quest=="1":
                        grade=input("gave your grade, gave it like that(,17,19,16):  ")
                        if not grade.startswith(","):
                            print("start it with ,")
                        else:
                            name3=input("gave the name: ")
                            cursor1.execute("UPDATE users SET grade =grade|| ? WHERE name=?",(grade,name3,))
                            connect1.commit()
                            
                    elif quest=="2":
                        name5=input("gave your name:  ")
                        name6=input("gave a new name: ")
                        cursor1.execute("UPDATE users SET name =name|| ? WHERE name=?",(name5,name6,))
                        connect1.commit()
                        
                    elif quest=="3":
                        name5=input("gave your name:  ")
                        grade2=int(input("gave a new grade: "))
                        if grade2 in range(0,21):
                            grade22=str(grade2)
                            cursor1.execute("UPDATE users SET grade =grade|| ? WHERE name=?",(grade22,name5,))
                            connect1.commit()
                            
                        else:
                            print("invalid value")
                    else:
                        print("there is something wrong")
            elif menu==5:
                questname=input("gave the name of student: ")
                cursor1.execute("SELECT * FROM users WHERE name=?",(questname,))
                result4=cursor1.fetchone()
                if result4 is not None:
                    cursor1.execute("DELETE FROM users WHERE name=?",(questname,))
                    connect1.commit()
                else:
                    invalid_name()
            else:
                print("good luck !")
                cursor1.close()
                break
                    








                

