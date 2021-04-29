from typing import List

from bundesliga.Team import Team, PRINT_FORMAT


class BColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# change int to str for table header
PREFIX = '{:<3d}'
FORMAT = (PREFIX + PRINT_FORMAT).replace('d', 's') + '\n'
WIDTH = 65


class Table:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def add_teams(self, t):
        if isinstance(t, List):
            for team in t:
                self.teams.append(team)
        elif isinstance(t, Team):
            self.teams.append(t)

    def _create_str(self, row, i):
        ret = PREFIX.format(i + 1) + row + "\n"
        if i < 4:
            ret = BColors.BLUE + ret + BColors.ENDC
        elif i == 4 or i == 15:
            ret = BColors.YELLOW + ret + BColors.ENDC
        elif i == 5:
            ret = BColors.GREEN + ret + BColors.ENDC
        elif i > 15:
            ret = BColors.RED + ret + BColors.ENDC
        return ret

    def show_table(self):
        sorted_teams = sorted(self.teams, reverse=True)
        rows = []
        for team in sorted_teams:
            rows.append(str(team))
        out = self.name + "\n"
        out += ''.join(['-' for _ in range(WIDTH)]) + "\n"
        out += FORMAT.format("", "Team", "Sp", "S", "U", "N", "T", "GT", "TD", "Pkt")
        for i, row in enumerate(rows):
            out += self._create_str(row, i)
        out += ''.join(['-' for _ in range(WIDTH)]) + "\n"
        return out

    def __str__(self):
        return self.show_table()


