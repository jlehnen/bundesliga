from numpy.random.mtrand import poisson

from bundesliga.Match import Matches, Match
from bundesliga.Table import Table
from bundesliga.Team import Team


if __name__ == '__main__':
    table = Table("Bundesliga")
    gladbach = Team("Borussia Moenchengladbach")
    dortmund = Team("Borussia Dortmund")
    hoffenheim = Team("Hoffenheim")
    leipzig = Team("RB Leipzig")
    bayern = Team("Bayern Muenchen")
    freiburg = Team("Freiburg")
    schalke = Team("Schalke")
    frankfurt = Team("Eintracht Frankfurt")
    wolfsburg = Team("Wolfsburg")
    leverkusen = Team("Leverkusen")
    hertha = Team("Hertha Berlin")
    bremen = Team("Werder Bremen")
    duesseldorf = Team("Fortuna Duesseldorf")
    union = Team("Union Berlin")
    mainz = Team("Mainz 05")
    augsburg = Team("Augsburg")
    koeln = Team("1. FC Koeln")
    paderborn = Team("SC Paderborn")
    table.add_teams([
        gladbach,
        dortmund,
        hoffenheim,
        leipzig,
        bayern,
        freiburg,
        schalke,
        frankfurt,
        wolfsburg,
        leverkusen,
        hertha,
        bremen,
        duesseldorf,
        union,
        mainz,
        augsburg,
        koeln,
        paderborn
    ])

    cheat = True
    for home in table.teams:
        for guest in table.teams:
            if home != guest:
                match = Match(home, guest,
                              [int(poisson(3)) if cheat and home == gladbach else int(poisson(2)),
                               int(poisson(3)) if cheat and guest == gladbach else int(poisson(2))])
                Matches.append(match)
                # print(match)

    print()
    print(table)
