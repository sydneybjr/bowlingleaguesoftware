import datetime as dt
import sqlite3 as sql

class Team:
    def __init__(self,TeamName):
        self.TeamName = TeamName
        con = sql.connect("BLS.db")
        cur = con.cursor()
        query = cur.execute("select coalesce(max(TeamID),0) as TeamID from Team")
        res = query.fetchone()
        self.TeamID = res[0] + 1
        
