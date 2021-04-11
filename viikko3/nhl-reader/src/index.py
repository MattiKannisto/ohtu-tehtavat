from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats
import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print("Players from FIN " + str(datetime.datetime.now()) + "\n")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
