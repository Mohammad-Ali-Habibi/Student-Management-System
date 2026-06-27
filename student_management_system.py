
import mysql.connector as sql
c1=sql.connect(host="localhost",
               user="root",
               password="",
               database="batman")
cu1=c1.cursor()
#cu1.execute("create table Add_Student (id int auto_increment primary key , name Varchar(100) , Avg float)")
def add_student():
        while True:
                try:
                   name = input("exit == 00 , Name : ")
                   if name == "00":
                        break
                   Avg = float(input("Avg : "))
                   if Avg <= 0:
                        print("Avg can't be Nagetive .")
                        continue
                   cu1.execute("insert into Add_Student (name , Avg) Values(%s,%s)",(name,Avg))
                   c1.commit()
                except ValueError:
                        print("Value Error.")
def show_student():
        cu1.execute("select * from Add_Student")
        rows = cu1.fetchall()
        for student_id, name, avg in rows:
                print(f"ID: {student_id}")
                print(f"Name: {name}")
                print(f"Avg: {avg}")
                print("-" * 20)
def delete_student():
     while True:
        Name = input("Exit == 00 , Name : ")
        if Name == "00":
             break
        cu1.execute("delete from Add_Student where name = %s",(Name,))
        c1.commit()
        if cu1.rowcount == 0:
             print("Student not found .")
        else:
             print("Student deleted.")
def update_student():
     while True :
        try:
             Name = input(" Exit == 00 , Name : ")
             if Name == "00":
                break
             Avg = float(input("Avg : "))
             if Avg <= 0 :
                print("Avg can't be Nagetive .")
                continue
             cu1.execute("update Add_Student set Avg = %s where name = %s",(Avg, Name))
             c1.commit()
             if cu1.rowcount == 0:
                print("Student not found .")
             else:
                print("Student status updated .")
        except ValueError:
             print("Value Error. ")
def search_student():
     while True:
        try:
             Name = input("Exit == 00 , Name : ")
             if Name == "00":
                break
             cu1.execute("select * from Add_Student where name = %s",(Name,))
             rows = cu1.fetchall()
             for student_id, name, avg in rows:
                print(f"ID: {student_id}")
                print(f"Name: {name}")
                print(f"Avg: {avg}")
                print("-" * 20)
             if rows == []:
                print("Student not found .")
        except ValueError:
             print("value Error .")
def top_student():
   cu1.execute("select * from Add_Student order by Avg desc limit 1 ;")
   row = cu1.fetchone()
   if row is None:
      print("student not found .")
   else:
      student_id , name , avg = row
      print(f"ID: {student_id}")
      print(f"Name: {name}")
      print(f"Avg: {avg}")
def average_student():
    cu1.execute("select avg(Avg) from Add_Student")
    row = cu1.fetchone()
    if row[0] is None:
        print("No students found.")
    else:
        print(f"Average : {row[0]}")
def main():
     while True :
        try:
             user = input("Exit == 0 , add_student == 1 , delete_student == 2 ,  search_student == 3 , show_student == 4 , update_student == 5  , average_student == 6 , top_student == 7 : ")
             if user == "0":
               break
             if user == "1":
               add_student()
             if user == "2":
               delete_student()
             if user == "3":
               search_student()
             if user == "4":
               show_student()
             if user == "5":
               update_student()
             if user == "6":
               average_student()
             if user == "7":
               top_student()
        except ValueError:
                print("Value Error . ")  
main()
c1.close()