def getAllTeams(games):
    teams = set()
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

def last6HomeStatAverage(games, teamId, before, stat):
    filtered = games[games["Date"] < before]
    if not filtered.empty:
        return filtered[filtered["HomeTeamID"] == teamId].iloc[-6:,:][stat].sum()
    return 0

def last6AwayStatAverage(games, teamId, before, stat):
    filtered = games[games["Date"] < before]
    if not filtered.empty:
        return filtered[filtered["AwayTeamID"] == teamId].iloc[-6:,:][stat].sum()
    return 0