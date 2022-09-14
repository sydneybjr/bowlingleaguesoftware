import datetime as dt
import sqlite3 as sql

class League:
    #Each bowling league must be initialized with a league name
    def __init__(self,name):
        self.name = name
        con = sql.connect("BLS.db")
        cur = con.cursor()
        query = cur.execute("select coalesce(max(LeagueID),0) as LeagueID from League")
        res = query.fetchone()
        self.LeagueID = res[0] + 1

    #Setting the start date of the league (datetime)
    def set_start_date(self,date):
        self.date = date
        self.day_of_week = date.weekday()

    #Setting the weeks of the season (integer value)
    def set_num_of_weeks(self,weeks):
        self.weeks = weeks

    #League rules section
    #Sets if match scoring will be used (bool)
    def set_match_scoring(self,match_scoring):
        self.match_scoring = match_scoring

    #Sets the percentage and base score to be used (float, int)
    def set_handicap(self,hdcp_percentage,hdcp_basis):
        self.hdcp_percentage = hdcp_percentage
        self.hdcp_basis

    #Sets if individual handicap is used (bool)
    def is_hdcp_individual(self,indv_hdcp):
        self.indv_hdcp = indv_hdcp

    #Sets the number of weeks average should be used (int)
    def set_establish_weeks(self,avg_weeks):
        self.avg_weeks = avg_weeks

    def set_points_per_game_team(self,Team_Game_Points):
        self.Team_Game_Points = Team_Game_Points

    def set_points_for_totals_team(self,Team_Series_Points):
        self.Team_Series_Points = Team_Series_Points

    def set_points_for_indv_match_game(self,Indv_Game_Match_Points):
        self.Indv_Game_Match_Points = Indv_Game_Match_Points

    def set_points_for_indv_match_series(self,Indv_Series_Match_Points):
        self.Indv_Series_Match_Points = Indv_Series_Match_Points
