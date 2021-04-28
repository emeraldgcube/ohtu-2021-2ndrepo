import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url=url
        self.players=[]
        self.read()

    def read(self):
        response = requests.get(self.url).json()
        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games']
            )

            self.players.append(player)

    def get_players(self):
        return self.players

class PlayerStats:
    def __init__(self, reader):
        self.reader=reader
        self.pelaajat=self.reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        all=self.pelaajat
        few=filter(lambda player: player.nationality==nationality, all)
        return reversed(sorted(few, key=lambda player: (player.goals + player.assists)))


def main():

#lopullinen
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
