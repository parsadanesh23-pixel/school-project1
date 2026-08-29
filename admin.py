from main import start
enter=input("gave your username: ")
password=input("enter password: ")
while enter!="admin1234" or password!="1234":
    enter=input("gave your username: ")
    password=input("enter password: ")
if enter=="admin1234" and password=="1234":
    start()