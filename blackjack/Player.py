class Player:

    def __init__(self, name):
        self.name = name
        self.points = 0

    def __str__(self):
        return "Player: {}; Points: {} // ".format(self.name, self.points)



