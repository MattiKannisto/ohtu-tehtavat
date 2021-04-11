from player import Player

class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.players

    def top_scorers_by_nationality(self, nationality):
        nationalitys_players = []

        for player in self.players:
            if player.nationality == nationality:
                nationalitys_players.append(player)

        top_scorers = sorted(nationalitys_players, key=lambda player: player.goals + player.assists, reverse=True)
        return top_scorers