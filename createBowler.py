import datetime as dt
import sqlite3 as sql


class Bowler:
    def __init__(self):
        con = sql.connect("BLS.db")
        cur = con.cursor()
        query = cur.execute("select coalesce(max(BowlerID),0) as BowlerID from Bowler")
        res = query.fetchone()
        self.bowlerID = res[0] + 1

    def set_bowler_first_name(self,FirstName):
        self.FirstName = FirstName

    def set_bowler_last_name(self,LastName):
        self.LastName = LastName
        
    def set_bowler_middle_initial(self,MiddleInitial):
        self.MiddleInitial = MiddleInitial

    def set_bowler_suffix(self,Suffix):
        self.Suffix = Suffix

    def set_bowler_book_average(self,BookAverage):
        self.BookAverage = BookAverage

    def set_bowler_book_games(self,BookGames):
        self.BookGames = BookGames

    def set_bowler_entering_average(self,EnteringAverage):
        self.EnteringAverage = EnteringAverage

    def set_bowler_entering_games(self,EnteringGames):
        self.EnteringGames = EnteringGames
