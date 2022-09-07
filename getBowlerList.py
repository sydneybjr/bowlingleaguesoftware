import sqlite3 as sql

class Bowler:
    def __init__(self,bowlerID,firstName,middleInitial,lastName,
                 enteringAverage,enteringGames,bookAverage,bookGames):
        self.bowlerID = bowlerID
        self.firstName = firstName
        self.middleInitial = middleInitial
        self.lastName = lastName
        self.enteringAverage = enteringAverage
        self.enteringGames = enteringGames
        self.bookAverage = bookAverage
        self.bookGames = bookGames

con = sql.connect("BLS.db")
cur = con.cursor()
bowlerList = []
bowlerObjects = []
bowlerQuery = cur.execute("select coalesce(bowlerID,0) as bowlerID, " +
                          "coalesce(firstName,'') as firstName, " +
                          "coalesce(middleInitial,'') as middleInitial, " +
                          "coalesce(lastName,'') as firstName, " +
                          "coalesce(enteringAverage,0) as enteringAverage, " +
                          "coalesce(enteringGames,0) as enteringGames, " +
                          "coalesce(bookAverage,0) as bookAverage, " +
                          "coalesce(bookGames,0) bookGames from Bowler")
bowlerDataset = bowlerQuery.fetchall()

for bowler in bowlerDataset:
    bowlerList.append(bowler)
    bowlerObjects.append(Bowler(bowler[0],bowler[1],bowler[2],bowler[3],
                                bowler[4],bowler[5],bowler[6],bowler[7]))

con.close()    

print(bowlerObjects[0].lastName)
