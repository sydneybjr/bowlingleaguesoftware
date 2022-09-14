import datetime as dt
import sqlite3 as sql

class Bowler:
    def __init__(self,ID):
        self.ID = ID

        if ID == 0:
            con = sql.connect("BLS.db")
            cur = con.cursor()
            query = cur.execute("select coalesce(max(BowlerID),0) BowlerID from Bowler")
            res = query.fetchone()
            self.ID = int(res[0]) + 1
            con.close()
        else:
            self.ID = ID

    def set_bowler_first_name(self,FirstName):
        self.first_name = FirstName

    def set_bowler_last_name(self,LastName):
        self.last_name = LastName
        
    def set_bowler_middle_initial(self,MiddleInitial):
        self.middle_initial = MiddleInitial

    def set_bowler_suffix(self,Suffix):
        self.suffix = Suffix

    def set_bowler_book_average(self,BookAverage):
        self.book_average = BookAverage

    def set_bowler_book_games(self,BookGames):
        self.book_games = BookGames

    def set_bowler_entering_average(self,EnteringAverage):
        self.entering_average = EnteringAverage

    def set_bowler_entering_games(self,EnteringGames):
        self.entering_games = EnteringGames
