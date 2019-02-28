"""Classes to make accessing object properties easier."""
import json
import string

def clean(s):
    """Returns a string retaining only letters and numbers."""
    return ''.join(c for c in s if c in string.ascii_letters + string.digits)

class Player:
    """A player part of a team."""
    def __init__(self, data):
        self.tag = data.get('tag')
        self.name = data.get('name')
        self.major = data.get('major')
        self.year = data.get('year')

class Team:
    """A team to be listed on the roster page."""
    def __init__(self, data):
        self.name = data.get('name')
        self.level = data.get('level')
        self.game = data.get('game')
        self.scores = data.get('scores')
        self.players = [Player(x) for x in data.get('players')]

    @property
    def _id(self):
        return clean(f'{self.game}-{self.name}')

    @property
    def get_score(self, date):
        """Gets the score for a given week if it exists."""
        return next((score.get('record') for score in self.scores if score.get('date') == date), '-')

    @property
    def record(self):
        """Returns the number of games won and lost."""
        result = lambda score: len([x for x in self.scores if x.get('result') == score])
        return f"{result('W')}-{result('L')}"

class Game:
    """A collection of teams for a game."""
    def __init__(self, data):
        self.name = data.get('name')
        self.logo = data.get('logo')
        self.dates = data.get('dates')
        self.teams = [Team(x) for x in data.get('teams')]

    @property
    def num_matches(self):
        """Returns the highest number of matches played by one team."""
        return max(len(team.scores) for team in self.teams)

def get_games():
    """Convenience function to parse JSON and return a list of game objects."""
    with open('app/data/teams.json') as f:
        raw_data = json.load(f)
    games = []
    for game, game_data in sorted(raw_data.items(), key=lambda x: x[1]['name']):
        games.append(Game(game_data))
    return games