class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def increment_points(self):
        self.score += 1

    def get_name(self):
        return self.name

    def get_points(self):
        return self.score