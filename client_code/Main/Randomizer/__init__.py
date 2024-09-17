from ._anvil_designer import RandomizerTemplate
from anvil import *

from random import choice, shuffle, randint

class Randomizer(RandomizerTemplate):

  ORANGE = '#F5D1B6'
  YELLOW = '#E7DDB4'
  GREEN = '#ABCCAD'
  BLUE = '#C8CFDE'
  PURPLE = '#B78FBE'

  PASS_HANDS = 'ABCDE'
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.players = [['Player 1', 'black', 'X'],
                    ['Player 2', 'black', 'X']]

    self.update_players()

  def update_players(self):
    self.players_repeating_panel.items = self.players
  
  def add_player_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    num_players = len(self.players)
    if num_players < 5:
      new_player = [f'Player {num_players+1}', 'black', 'X']
      self.players.append(new_player)
      self.remove_player_button.background = 'white'
      if num_players == 4:
        self.add_player_button.background = 'lightgrey'
    self.update_players()

  def remove_player_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    num_players = len(self.players)
    if num_players > 2:
      self.players.pop(-1)
      self.add_player_button.background = 'white'
      if num_players == 3:
        self.remove_player_button.background = 'lightgrey'
    self.update_players()

  def randomize_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    colors = [self.ORANGE, self.YELLOW, self.GREEN, self.BLUE, self.PURPLE]
    shuffle(colors)
    offset = randint(0, 4)
    num_players = len(self.players)
    for i, player in enumerate(self.players):
      player[1] = colors.pop()
      player[2] = self.PASS_HANDS[(i+offset)%num_players]
    self.update_players()
    self.first_sanctuary_pick.text = choice(self.players)[0]