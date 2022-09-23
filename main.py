import nfl_espn_api


if __name__ == '__main__':
    n = nfl_espn_api.EspnApi()
    team = nfl_espn_api.EspnTeam('5')
    for k,v in team.team_info()['team'].items():
        print(f'{k}: {v}')
