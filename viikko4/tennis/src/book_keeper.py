import player

class BookKeeper:
    def __init__(self, player_1_name, player_2_name):
        self.players = [player.Player(player_1_name), player.Player(player_2_name)]

    def add_point(self, name):
        for player in self.players:
            if player.get_name() == name:
                player.increment_points()
    
    def tell_all_points(self):
        all_points = []
        for player in self.players:
            all_points.append(player.get_points())
        return all_points

    def check_who_is_in_lead(self):
        top_scorer = player.Player("")
        for _player in self.players:
            if _player.get_points() >= top_scorer.get_points():
                top_scorer = _player
        return top_scorer

    def check_if_draw(self):
        for player in self.players:
            if player.get_points() != self.check_who_is_in_lead().get_points():
                return False
        return True
    
    def check_if_advantage(self):
        for player in self.players:
            if abs(self.check_who_is_in_lead().get_points() - player.get_points()) == 1:
                return True
        return False

    def check_if_either_player_is_about_to_win(self, points_needed_to_win):
        for player in self.players:
            if player.get_points() >= points_needed_to_win:
                return True
        return False
