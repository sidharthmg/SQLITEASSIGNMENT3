import sqlite3
conn=sqlite3.connect("Database.sqlite")
cursor=conn.cursor()
def count():
    cursor.execute("SELECT COUNT (*) FROM Teams")
    teamcount=cursor.fetchall()
    print("\n Number of rown in Teams table",teamcount)

def uniqueseason():
    cursor.execute("SELECT DISTINCT (Season) FROM Teams")
    unique=cursor.fetchall()
    print("\n Unique values in Season column",unique)

def stadiumcap():
    cursor.execute("SELECT MAX(StadiumCapacity),MIN(StadiumCapacity) FROM Teams")
    stadiumcapacity = cursor.fetchall()
    print("\n The largest and smallest seating capacities are",stadiumcapacity)

def sumsquad():
    cursor.execute("SELECT SUM(KaderHome) AS Total_Soccer_Players FROM Teams WHERE Season=2014")
    sumsquad=cursor.fetchall()
    print("\n The total sum of squad players for 2014 is",sumsquad)

def homemanu():
    cursor.execute("SELECT ROUND(AVG(FTHG),2) AS Avg_Homegoals FROM Matches WHERE HomeTeam='Man United' ")
    avghomegoals=cursor.fetchall()
    print("\n Average home goals for Man United", avghomegoals)

f=True
while f:
     print("\n Enter 1 to Counts all the rows in the Teams table"
           "\n 2 to see all the unique values that are included in the Season column in the Teams table"
           "\n 3 to see the largest and smallest stadium capacity that is included in the Teams table"
           "\n 4 to see the sum of squad players for all teams during the 2014 season from the Teams table "
           "\n 5 to know how many goals did Man United score during home games on average? "
           "\n 6 to exit")
     ch = int(input("Enter the number:"))
     if ch == 1:
         count()
     if ch==2:
         uniqueseason()
     if ch==3:
         stadiumcap()
     if ch==4:
         sumsquad()
     if ch==5:
         homemanu()
     elif ch==6:
         f=False
conn.commit()
conn.close()

