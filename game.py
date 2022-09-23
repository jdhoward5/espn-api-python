import nfl_espn_api
import database
import sqlite3

def create_tables(conn: sqlite3.Connection) -> None:
    query = '''
    CREATE TABLE IF NOT EXISTS game (
        event_id INTEGER PRIMARY KEY,
        uid TEXT NOT NULL,
        date TEXT NOT NULL,
        name TEXT NOT NULL,
        short_name TEXT NOT NULL,
        season TEXT,
        season_type TEXT,
        week TEXT,
        team_a_id INTEGER NOT NULL,
        team_b_id INTEGER NOT NULL,
        FOREIGN KEY (team_a_id) REFERENCES teams (id)
        FOREIGN KEY (team_b_id) REFERENCES teams (id)
    );
    '''
    database.execute_query(conn, query)

class Game(object):
    def __init__(self, event: nfl_espn_api.EspnCompetitions) -> None:
        self.connection = database.create_connection('database.sqlite')
        self.event = event
        create_tables(self.connection)
        

if __name__ == '__main__':
    pass