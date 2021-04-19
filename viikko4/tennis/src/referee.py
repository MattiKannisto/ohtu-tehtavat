class Referee:
    def __init__(self):
        self.points_in_words = ["Love", "Fifteen", "Thirty", "Forty"]

    def announce_points(self, points_in_numbers):
        announcement = self.points_in_words[points_in_numbers[0]] + "-"
        if points_in_numbers[0] == points_in_numbers[1]:
            announcement += "All"
        else:
            announcement += self.points_in_words[points_in_numbers[1]]
        return announcement

    def remind_how_many_points_are_needed_to_win(self):
        return len(self.points_in_words)

    def announce_advantage_for_player(self, player_name):
        return "Advantage " + player_name

    def announce_deuce(self):
        return "Deuce"

    def announce_winner(self, player_name):
        return "Win for " + player_name