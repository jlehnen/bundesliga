FORMAT = '{:27s} {:3>d} : {:<3d} {:30s}'


class Match:
    def __init__(self, home, guest, score):
        self.home = home
        self.guest = guest
        self.score = score
        self.home.plays(self.guest, self.score)

    def __str__(self):
        return FORMAT.format(self.home.name, self.score[0], self.score[1], self.guest.name)

    def __repr__(self):
        return f"{self.score} {self.guest.name}"


class Matches:
    history = {}

    @classmethod
    def append(cls, match):
        if cls.history.get(match.home.name) is None:
            cls.history[match.home.name] = []
        cls.history[match.home.name].append(match)
