import nfl_espn_api


if __name__ == '__main__':
    n = nfl_espn_api.EspnApi()
    for team_id in n.get_team_ids():
        team = nfl_espn_api.EspnTeam(str(team_id))
        print(team.team_roster())
        print()
