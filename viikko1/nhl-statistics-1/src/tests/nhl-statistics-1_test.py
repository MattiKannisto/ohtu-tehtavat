import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_player_list_is_of_correct_size(self):
        self.assertEqual(len(self.statistics._players), 5)

    def test_player_list_is_positive_in_size(self):
        self.assertGreater(len(self.statistics._players), 0)

    def test_search_finds_existing_player(self):
        searched_player = Player("Kurri",   "EDM", 37, 53)
        self.assertEqual(str(self.statistics.search("Kurri")), str(searched_player))

    def test_search_returns_none_when_searching_nonexistent_player(self):
        self.assertEqual(self.statistics.search("Nonexistent"), None)

    def test_team_search_returns_correct_players(self):
        searched_player_names = ["Semenko", "Kurri", "Gretzky"]
        obtained_list = self.statistics.team("EDM")
        obtained_player_names = []
        for player in obtained_list:
            obtained_player_names.append(player.name)
        self.assertEqual(str(obtained_player_names), str(searched_player_names))

    def test_team_search_returns_none_when_searching_for_nonexistent_team(self):
        self.assertEqual(len(self.statistics.team("Nonexistent")), 0)

    def test_top_scores_returns_empty_list_with_negative_number_of_players(self):
        self.assertEqual(len(self.statistics.top_scorers(-1)), 0)

    def test_top_scores_returns_top_scorer_order_correctly(self):
        correct_top_scorer_order = ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]
        obtained_player_list = self.statistics.top_scorers(4)
        obtained_player_names = []
        for player in obtained_player_list:
            obtained_player_names.append(player.name)
        self.assertEqual(str(obtained_player_names), str(correct_top_scorer_order))
