from urllib.parse import urlparse
import requests

class EspnApi:
    def __init__(self) -> None:
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'
        self.hdr = {'user-agent': self.user_agent}
        self.base = 'https://site.web.api.espn.com'
        self.sport_core = 'https://sports.core.api.espn.com'
    
    def search(self) -> any:
        url = f'{self.base}/apis/common/v3/search'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def fantasy_games(self, date_from: str, date_to: str) -> any:
        url = f'{self.base}/apis/fantasy/v2/games/ffl/games'
        pld = {'dates': f'{date_from}-{date_to}'}
        
        r = requests.get(url, params=pld, headers=self.hdr)
        return r.json()
    
    def scoreboard_header(self, sport='football', league='nfl') -> any:
        url = f'{self.base}/apis/v2/scoreboard/header'
        pld = {'sport': sport, 'league': league}
        
        r = requests.get(url, params=pld, headers=self.hdr)
        return r.json()
    
    def nfl_info(self) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl'
        
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def calendar(self) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/calendar'
        
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def calendar_blacklist(self) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/calendar/blacklist'
        
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def calendar_whitelist(self) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/calendar/whitelist'
        
        r = requests.get(url, headers=self.hdr)
        return r.json()

    def get_events(self) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/events'
        
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_event_ids(self) -> list:
        data = self.get_events()['items']
        urls = [d['$ref'] for d in data]
        return list(map(lambda url: urlparse(url).path.split('/')[-1], urls))
    
    def event_info(self, event_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/events/{event_id}'
        
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def event_competitions(self, event_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/events/{event_id}/competitions/{event_id}'
        
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def group_standings(self, group_id: str, season_type: str, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/groups/{group_id}/standings'
        
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def group_teams(self, group_id: str, season_type: str, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/groups/{group_id}/teams'
        
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def leaders(self, season: str) -> any:
        url = f'{self.base}/apis/site/v3/sports/football/nfl/leaders'
        pld = {'season': season}
        
        r = requests.get(url, params=pld, headers=self.hdr)
        return r.json()
    
    def leaders(self) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/leaders'
        
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def leaders_v2(self) -> any:
        url = f'{self.sport_core}/v2/sports/football/leageus/nfl/leaders/0'
        
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def news(self) -> any:
        url = f'{self.base}/apis/site/v2/sports/football/nfl/news'
        
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def odd_predictors(self, event_id: str, provider_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/events/{event_id}/competitions/{event_id}/odds/{provider_id}/predictors'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def positions(self, position_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/positions/{position_id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_position_ids(self, limit=100) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/positions'
        pld = {'limit': limit}
        r = requests.get(url, params=pld, headers=self.hdr)
        return r.json()

    def providers(self, provider_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/providers/{provider_id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def scoreboard(self) -> any:
        url = f'{self.base}/apis/site/v2/sports/football/nfl/scoreboard'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def seasons(self) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def season_year(self, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}'
        r = requests.get(url, headers=self.hdr)
        return r.json()

    def season_coaches(self, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/coaches'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def season_coaches(self, year: str, coach_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/coaches/{coach_id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def season_draft(self, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/draft'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def season_futures(self, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/futures'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def season_futures(self, year: str, future_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/futures/{future_id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def season_teams(self, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/teams'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def season_teams(self, year: str, team_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/teams/{team_id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def season_types(self, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def season_types(self, year: str, season_type: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def talentpicks(self) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/talentpicks'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def teams(self, limit=32) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/teams'
        pld = {'limit': limit}
        r = requests.get(url, params=pld, headers=self.hdr)
        return r.json()
    
    def get_team_ids(self, limit=32) -> list:
        data = self.teams(limit)['items']
        urls = [d['$ref'] for d in data]
        return list(map(lambda url: urlparse(url).path.split('/')[-1], urls))
    
    def seasontype_groups(self, year: str, season_type: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/groups'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def seasontype_groups(self, year: str, season_type: str, group_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/groups/{group_id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def seasontype_leaders(self, year: str, season_type: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/leaders'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def seasontype_weeks(self, year: str, season_type: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/weeks'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def seasontype_weeks(self, year: str, season_type: str, week_num: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/weeks/{week_num}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def venues(self, venue_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/venues/{venue_id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_venue_ids(self, limit=700) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/venues'
        pld = {'limit': limit}
        r = requests.get(url, params=pld, headers=self.hdr)
        return r.json()
    
    def weekly_events(self, year: str, season_type: str, week_num: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/weeks/{week_num}/events'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def weekly_qbr(self, year: str, season_type: str, week_num: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/weeks/{week_num}/qbr/10000'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def weekly_talentpicks(self, year: str, season_type: str, week_num: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/weeks/{week_num}/talentpicks'
        r = requests.get(url, headers=self.hdr)
        return r.json()


class EspnAthletes(EspnApi):
    def __init__(self) -> None:
        super().__init__()
    
    def get_athlete_info(self, limit=1000) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/athletes'
        pld = {'limit': limit}
        r = requests.get(url, params=pld, headers=self.hdr)
        return r.json()['items']

    def get_athlete_ids(self, limit=1000) -> list:
        data = self.get_athlete_info(limit)
        urls = [d['$ref'] for d in data]
        return list(map(lambda url: urlparse(url).path.split('/')[-1], urls))

    def get_athletes(self, limit=1000) -> any:
        for d in self.get_athlete_info(limit):
            url = d['$ref']
            r = requests.get(url, headers=self.hdr)
            yield r.json()
    
    def get_athlete(self, id: str) -> any:
        url = f'{self.base}/apis/common/v3/sports/football/nfl/athletes/{id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_athlete_v2(self, id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/athletes/{id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_athlete_bio(self, id: str) -> any:
        url = f'{self.base}/apis/common/v3/sports/football/nfl/athletes/{id}/bio'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_athlete_eventlog(self, id: str, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/athletes/{id}/eventlog'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_athlete_gamelog(self, id: str) -> any:
        url = f'{self.base}/apis/common/v3/sports/football/nfl/athletes/{id}/gamelog'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_athlete_notes(self, id: str, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/athletes/{id}/notes'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_athlete_projections(self, id: str, season_type: str, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/athletes/{id}/projections'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_athlete_splits(self, id: str) -> any:
        url = f'{self.base}/apis/common/v3/sports/football/nfl/athletes/{id}/splits'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_athlete_stats(self, id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/athletes/{id}/statistics/0'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_athlete_stats_by_season(self, id: str, season_type: str, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/athletes/{id}/statistics'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_athlete_statslog(self, id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/athletes/{id}/statisticslog'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def get_athlete_stats_v3(self, id: str) -> any:
        url = f'{self.base}/apis/common/v3/sports/football/nfl/athletes/{id}/stats'       
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def season_athletes(self, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/athletes'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def season_athletes(self, year: str, id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/athletes/{id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()


class EspnCompetitions(EspnApi):
    def __init__(self, event_id: str) -> None:
        super().__init__()
        self.event_id = event_id
    
    def competition_drives(self, drive_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/events/{self.event_id}/competitions/{self.event_id}/drives/{drive_id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def competition_odds(self) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/events/{self.event_id}/competitions/{self.event_id}/odds'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def competition_odds(self, provider_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/events/{self.event_id}/competitions/{self.event_id}/odds/{provider_id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def competition_plays(self, limit=200) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/events/{self.event_id}/competitions/{self.event_id}/plays'
        pld = {'limit': limit}
        r = requests.get(url, params=pld, headers=self.hdr)
        return r.json()
    
    def competition_plays(self, play_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/events/{self.event_id}/competitions/{self.event_id}/plays/{play_id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def competition_probabilities(self, limit=200) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/events/{self.event_id}/competitions/{self.event_id}/probabilities'
        pld = {'limit': limit}
        r = requests.get(url, params=pld, headers=self.hdr)
        return r.json()
    
    def competition_probabilities(self, probabilities_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/events/{self.event_id}/competitions/{self.event_id}/probabilities/{probabilities_id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def competitor_roster(self, competitors_id: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/events/{self.event_id}/competitions/{self.event_id}/competitors/{competitors_id}/roster'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    

class EspnDraft(EspnApi):
    def __init__(self, year: str) -> None:
        super().__init__()
        self.year = year
    
    def draft_athletes(self, limit=500) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{self.year}/draft/athletes'
        pld = {'limit': limit}
        r = requests.get(url, params=pld, headers=self.hdr)
        return r.json()
    
    def draft_rounds(self) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{self.year}/draft/rounds'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def draft_status(self) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{self.year}/draft/status'
        r = requests.get(url, headers=self.hdr)
        return r.json()


class EspnFranchises(EspnApi):
    def __init__(self) -> None:
        super().__init__()
    
    def get_franchises(self) -> str:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/franchises'
        r = requests.get(url, headers=self.hdr)
        data = r.json()['items']
        for d in data:
            yield d['$ref']
    
    def get_franchise_ids(self) -> list:
        urls = [u for u in self.get_franchises()]
        return list(map(lambda url: urlparse(url).path.split('/')[-1], urls))

class EspnTeam(EspnApi):
    def __init__(self, team_id: str) -> None:
        super().__init__()
        self.team_id = team_id
    
    def team_info(self) -> any:
        url = f'{self.base}/apis/site/v2/sports/football/nfl/teams/{self.team_id}'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_athletes(self, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/teams/{self.team_id}/athletes'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_ats(self, year: str, season_type: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/teams/{self.team_id}/ats'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_attendance(self, year: str, season_type: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/teams/{self.team_id}/attendance'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_coaches(self, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/teams/{self.team_id}/coaches'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_depthcharts(self, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/teams/{self.team_id}/depthcharts'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_events(self, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/teams/{self.team_id}/events'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_injuries(self) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/teams/{self.team_id}/injuries'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_leaders(self, year: str, season_type: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/teams/{self.team_id}/leaders'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_odds_records(self, year: str, season_type: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/teams/{self.team_id}/odds-records'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_projection(self, year: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/teams/{self.team_id}/projection'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_record(self, year: str, season_type: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/teams/{self.team_id}/record'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_roster(self) -> any:
        url = f'{self.base}/apis/site/v2/sports/football/nfl/teams/{self.team_id}/roster'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_schedule(self) -> any:
        url = f'{self.base}/apis/site/v2/sports/football/nfl/teams/{self.team_id}/schedule'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
    def team_statistics(self, year: str, season_type: str) -> any:
        url = f'{self.sport_core}/v2/sports/football/leagues/nfl/seasons/{year}/types/{season_type}/teams/{self.team_id}/statistics'
        r = requests.get(url, headers=self.hdr)
        return r.json()
    
