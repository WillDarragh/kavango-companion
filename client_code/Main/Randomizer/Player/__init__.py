from ._anvil_designer import PlayerTemplate
from anvil import *

class Player(PlayerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.player_name.placeholder = self.item[0]
    self.board_color.background = self.item[1]
    self.pass_hand.text = self.item[2]

  def player_name_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.item[0] = self.player_name.text

