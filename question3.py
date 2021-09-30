import sqlite3
conn=sqlite3.connect("Database.sqlite")
cursor=conn.cursor()
def HomeTeam():
    cursor.execute("SELECT HomeTeam,FTHG,FTAG FROM Matches WHERE HomeTeam='Aachen' AND  Season=2010 ORDER BY FTHG DESC")
    hometeam = cursor.fetchall()
    print("\n Aachen as Home Team,FTHG and FTAG from 2010", hometeam)

def totalhomegames():
    cursor.execute("SELECT HomeTeam, COUNT(FTR) FROM Matches WHERE FTR='H' AND Season=2016 GROUP BY HomeTeam ORDER BY COUNT(FTR) DESC")
    totalgames=cursor.fetchall()
    print("\n  Total number of home games each team won during the 2016 season",totalgames)

def tenrows():
    cursor.execute("SELECT * FROM Unique_Teams LIMIT 10")
    rows=cursor.fetchall()
    print("\n The first ten rows from the UniqueTeams table",rows)

def matchteam():
    cursor.execute("SELECT * FROM Teams_in_Matches T,Unique_Teams U WHERE  T.Unique_Team_ID = U.Unique_Team_ID")
    matchteams = cursor.fetchall()
    print("\n Match ID and Unique Team ID with Team_Name",matchteams)

def uniqueteam():
    cursor.execute("SELECT * FROM Unique_Teams U JOIN Teams T  ON U.TeamName = T.TeamName LIMIT 10")
    uniqueteams = cursor.fetchall()
    print("\n Ten rows of both tables are ",uniqueteams)

def fiverows():
    cursor.execute( "SELECT U.Unique_Team_ID,U.TeamName,T.AvgAgeHome,T.Season, T.ForeignPlayersHome FROM Unique_Teams U JOIN"
                    " Teams T  ON U.TeamName = T.TeamName LIMIT 5")
    thefiverows=cursor.fetchall()
    print("\n The required five rows are", thefiverows)

def highestmatch():
    cursor.execute("SELECT MAX(Match_ID),T.Unique_Team_ID,TeamName FROM Teams_in_Matches T JOIN Unique_Teams U "
                   "ON T.Unique_Team_ID =U.Unique_TEAM_ID WHERE (TeamName lIKE '%y')OR"
                   "(TeamName LIKE '%r')GROUP BY T.Unique_Team_ID,TeamName")
    highmatch = cursor.fetchall()
    print("\n tHE REQUIRED HIGHEST MATCH id",highmatch)

f = True
while f:
        print("\n Enter 1 to see the hometeam,FTHG,FTAG from 2010 of Aachen"
              "\n 2 to see the total number of home games each team won during the 2016 season"
              "\n 3 to see  the first ten rows from the Unique_Teams table"
              "\n 4 to see Match_ID and Unique_Team_ID with the corresponding Team_Name from the Unique_Teams and Teams_in_Matches tables"
              "\n 5 to join together the Unique_Teams data table and the Teams table, and returns the first 10 rows."
              "\n 6 to see  Unique_Team_ID and TeamName from the Unique_Teams table and AvgAgeHome, Season and ForeignPlayersHome from the Teams table "
              "\n 7 to see  highest Match_ID for each team that ends in a 'y' or a 'r' "
              "\n 8 to exit")
        ch = int(input("Enter the number:"))
        if ch == 1:
            HomeTeam()
        if ch == 2:
            totalhomegames()
        if ch == 3:
            tenrows()
        if ch == 4:
            matchteam()
        if ch == 5:
            uniqueteam()
        if ch == 6:
            fiverows()
        if ch == 7:
            highestmatch()
        elif ch == 8:
            f=False
conn.commit()
conn.close()
