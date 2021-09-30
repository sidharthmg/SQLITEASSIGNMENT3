import sqlite3
conn=sqlite3.connect("database.sqlite")
cursor=conn.cursor()
def homeawaylist():
    cursor.execute("SELECT HomeTeam,AwayTeam FROM Matches WHERE Season=2015 AND FTHG=5")
    homeaway=cursor.fetchall()
    print("\n Name of Home and away teams in 2015 season whereFull Time Home Goals were 5 are")
    for row in homeaway:
        print("\n Home Teams are", row[0])
        print("\n Away Teams are",row[1])

def arsenelawaywins():
    cursor.execute("SELECT * FROM Matches WHERE HomeTeam='Arsenel' AND FTR='A'")
    arsenelaway=cursor.fetchall()
    print("\n Details of Matches where Arsenel was home team and Full Time Result is an Away Win")
    for row in arsenelaway:
        print("\n Match ID", row[0])
        print("\n Division", row[1])
        print("\n Season", row[2])
        print("\n Date", row[3])
        print("\n Home Team", row[4])
        print("\n Away Team",row[5])
        print("\n Full Time Home Goals", row[6])
        print("\n Full Time Away Goals",row[7])
        print("\n Full Time Result", row[8])

def awaybayern():
    cursor.execute("SELECT * FROM Matches WHERE Season BETWEEN 2012 AND 2015 AND AwayTeam='Bayern Munich' AND FTHG > 2")
    awaybayern=cursor.fetchall()
    print("\n Details of Matches from 2012 to 2015 where Bayern was the home tam and full time home goals >2")
    for row in awaybayern:
        print("\n Match ID", row[0])
        print("\n Division", row[1])
        print("\n Season", row[2])
        print("\n Date", row[3])
        print("\n Home Team", row[4])
        print("\n Away Team",row[5])
        print("\n Full Time Home Goals", row[6])
        print("\n Full Time Away Goals",row[7])
        print("\n Full Time Result", row[8])

def AM():
    cursor.execute("SELECT * FROM Matches WHERE HomeTeam LIKE 'A%' AND AwayTeam LIKE 'M%                                                                                                               ' ")
    details=cursor.fetchall()
    print("\n Details of Matches where Home Team name starts with A and Away Team name begins with M")
    for row in details:
        print("\n Match ID", row[0])
        print("\n Division", row[1])
        print("\n Season", row[2])
        print("\n Date", row[3])
        print("\n Home Team", row[4])
        print("\n Away Team", row[5])
        print("\n Full Time Home Goals", row[6])
        print("\n Full Time Away Goals", row[7])
        print("\n Full Time Result", row[8])

f=True
while f:
     print("\n Enter 1 to see the names of both the Home Teams and Away Teams in each match played in 2015 and Full time Home Goals were 5"
           "\n 2 to see the details of the matches where Arsenal is the Home Team and  Full Time Result is an Away Win"
           "\n 3 to see all the matches from the 2012 season till the 2015 season where Away Team is Bayern Munich and Full time Away Goals > 2"
           "\n 4 to see all the matches where the Home Team name begins with 'A' and Away Team name begins with 'M'"
           "\n 5 to exit")
     ch = int(input("Enter the number:"))
     if ch == 1:
         homeawaylist()
     if ch==2:
         arsenelawaywins()
     if ch==3:
         awaybayern()
     if ch==4:
         AM()
     elif ch==5:
         f=False
conn.commit()
conn.close()
