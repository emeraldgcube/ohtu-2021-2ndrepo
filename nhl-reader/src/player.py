class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality=nationality
        self.assists=assists
        self.goals=goals
        self.penalties=penalties
        self.team=team
        self.games=games
    
    def __str__(self):
        loru= f"{self.name:20} {self.nationality}, {str(self.goals)} + {str(self.assists)}, {str(self.games)} peliä"
        return loru
