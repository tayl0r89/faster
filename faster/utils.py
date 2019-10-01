def getAllTeams(games):
    for team in games["HomeTeam"].values:
    teams.add(team)
    teamDict = {}
    count = 0
    for team in sorted(teams):
        teamDict[team] = count
        count = count + 1
    return teamDict