"""Classes to make accessing object properties easier."""
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
        self.players = [Player(x) for x in data.get('players')]

    @property
    def _id(self):
        return clean(f'{self.game}-{self.name}')

class Game:
    """A collection of teams for a game."""
    def __init__(self, data):
        self.name = data.get('name')
        self.logo = data.get('logo')
        self.teams = [Team(x) for x in data.get('teams')]