from calendar import c
from itertools import count
import sqlite3 as sql
import datetime as dt
from tkinter import E
from createBowler import Bowler as B

con = sql.connect("BLS.db")
cur = con.cursor()
query = cur.execute("select coalesce(BowlerID,0) as BowlerID, " + 
                    "coalesce(FirstName,'') as FirstName, " +
                    "coalesce(MiddleInitial,'') as MiddleInitial, " +
                    "coalesce(LastName,'') as LastName, " +
                    "coalesce(Suffix,'') as Suffix, " +
                    "coalesce(BookAverage,0) as BookAverage, " +
                    "coalesce(BookGames,0) as BookGames, " +
                    "coalesce(EnteringAverage,0) as EnteringAverage, " +
                    "coalesce(EnteringGames,0) as EnteringGames from Bowler")
res = query.fetchall()

counter = 0
bowler_List = []

for items in res:
    Bowler_ID, First_Name, Middle_Initial, Last_Name, Suffix, Book_Average, Book_Games, Entering_Average, Entering_Games = items
    bowler_List.append(B(Bowler_ID))
    bowler_List[counter].set_bowler_first_name(First_Name)
    bowler_List[counter].set_bowler_middle_initial(Middle_Initial)
    bowler_List[counter].set_bowler_last_name(Last_Name)
    bowler_List[counter].set_bowler_suffix(Suffix)
    bowler_List[counter].set_bowler_book_average(Book_Average)
    bowler_List[counter].set_bowler_book_games(Book_Games)
    bowler_List[counter].set_bowler_entering_average(Entering_Average)
    bowler_List[counter].set_bowler_entering_games(Entering_Games)
    counter += 1

for bowlers in bowler_List:
    print(bowlers.last_name)

con.close()    