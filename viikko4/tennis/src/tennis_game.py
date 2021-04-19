import book_keeper
import referee

class TennisGame:
    def __init__(self, player_1_name, player_2_name):
        self.book_keeper = book_keeper.BookKeeper(player_1_name, player_2_name) # Pitää kirjaa pelaajista ja heidän pisteistään
        self.referee = referee.Referee() # Huutelee pistetilanteita ja muistuttaa kirjanpitäjää monellako pisteellä voittaa
        
    def won_point(self, player_name):
        self.book_keeper.add_point(player_name)
        
    def get_score(self):
        if self.book_keeper.check_if_either_player_is_about_to_win(self.referee.remind_how_many_points_are_needed_to_win()):
            if self.book_keeper.check_if_advantage():
                score = self.referee.announce_advantage_for_player(self.book_keeper.check_who_is_in_lead().get_name())
            elif self.book_keeper.check_if_draw():
                score = self.referee.announce_deuce()
            else:
                score = self.referee.announce_winner(self.book_keeper.check_who_is_in_lead().get_name())
        else:
            score = self.referee.announce_points(self.book_keeper.tell_all_points())
        return score