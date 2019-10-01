def getAllTeams(games):
    for team in games["HomeTeam"].values:
    teams.add(team)
    teamDict = {}
    count = 0
    for team in sorted(teams):
        teamDict[team] = count
        count = count + 1
    return teamDict

def getRushSeries(games):
    return ((games["FTHG"] > 0) & (games["FTAG"] > 0)).map(lambda x: 1 if x else 0)