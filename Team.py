# start: 12:00, stop: 12:50 MVP
from bundesliga.Match import Matches

WIN_SCORE = 3
DRAW_SCORE = 1
PRINT_FORMAT = '{:30s} {:<3d} {:<3d} {:<3d} {:<3d} {:<3d} {:<3d} {:<3d} {:<3d}'


class Team:

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.games = 0
        self.goals = 0
        self.against = 0
        self.wins = 0
        self.draws = 0
        self.defeats = 0

    def goal_diff(self):
        return self.goals - self.against

    def plays(self, other, score):
        self.games += 1
        other.games += 1

        self.goals += score[0]
        self.against += score[1]
        other.goals += score[1]
        other.against += score[0]

        # self wins
        if score[0] > score[1]:
            self.wins += 1
            other.defeats += 1
            self.points += WIN_SCORE
        elif score[0] < score[1]:
            self.defeats += 1
            other.wins += 1
            other.points += WIN_SCORE
        else:
            self.draws += 1
            other.draws += 1
            self.points += DRAW_SCORE
            other.points += DRAW_SCORE
        return score

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        if self.points > other.points:
            return False
        elif self.points < other.points:
            return True
        else:
            if self.goal_diff() > other.goal_diff():
                return False
            elif self.goal_diff() < other.goal_diff():
                return True
            else:
                if self.goals > other.goals:
                    return False
                elif self.goals < other.goals:
                    return True
                else:
                    # direct comparison
                    total_score = [0, 0]
                    h, g = Matches.history[self.name], Matches.history[other.name]
                    for n in h:
                        if n.guest == other:
                            total_score[0] += n.score[0]
                            total_score[1] += n.score[1]
                    for n in g:
                        if n.guest == self:
                            total_score[0] += n.score[1]
                            total_score[1] += n.score[0]
                    return total_score[0] < total_score[1]

    def __str__(self):
        return PRINT_FORMAT.format(
            self.name, self.games, self.wins, self.draws, self.defeats, self.goals, self.against, self.goal_diff(), self.points
        )
