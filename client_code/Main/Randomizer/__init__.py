from ._anvil_designer import RandomizerTemplate
from anvil import *

from random import choice, shuffle, randint

class Randomizer(RandomizerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.players = [['Player 1', 'black', 'X'],
                    ['Player 2', 'black', 'X']]

    self.players_repeating_panel.items = self.players

  def update_players(self):
    self.players_repeating_panel.items = self.players
  
  def add_player_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    num_players = len(self.players)
    if num_players < 5:
      new_player = [f'Player {num_players+1}', 'black', 'X']
      self.players.append(new_player)
    self.update_players()

  def remove_player_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    num_players = len(self.players)
    if num_players > 2:
      self.players.pop(-1)
    self.update_players()

  def randomize_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

