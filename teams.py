import nfl_espn_api
import database
import sqlite3

def create_tables(conn: sqlite3.Connection) -> None:
    query = '''
    CREATE TABLE IF NOT EXISTS team (
        team_id INTEGER NOT NULL PRIMARY KEY,
        uid TEXT NOT NULL,
        slug TEXT NOT NULL,
        location TEXT NOT NULL,
        name TEXT NOT NULL,
        nickname TEXT NOT NULL,
        abbreviation TEXT NOT NULL,
        display_name TEXT NOT NULL,
        short_display_name TEXT NOT NULL,
        color TEXT NOT NULL,
        alternate_color TEXT,
        active BOOLEAN,
        logos TEXT,
        record TEXT,
        standing_summary TEXT
    );
    '''
    database.execute_query(conn, query)

class Team(object):
    def __init__(self, team: nfl_espn_api.EspnTeam) -> None:
        self.connection = database.create_connection('database.sqlite')
        self.team = team
        create_tables(self.connection)
        

if __name__ == '__main__':
    pass