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
    def __init__(self, data, game):
        self.name = data.get('name')
        self.scores = data.get('scores')
        self.game = game
        self.players = [Player(x) for x in data.get('players')]

    @property
    def _id(self):
        return clean(f'{self.game}-{self.name}')

    @property
    def record(self):
        """Returns the number of games won and lost."""
        scores = [w - l for w, l in [map(int, score.get('record').split('-')) for score in self.scores]]
        wins = len([x for x in scores if x > 0])
        losses = len([x for x in scores if x < 0])
        return f"{wins}-{losses}"

class Game:
    """A collection of teams for a game."""
    def __init__(self, data):
        self.name = data.get('name')
        self.alias = data.get('alias')
        self.logo = data.get('logo')
        self.dates = data.get('dates')
        self.teams = [Team(x, self.alias) for x in data.get('teams')]

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