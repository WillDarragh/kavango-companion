from ._anvil_designer import PlayerTemplateTemplate
from anvil import *


class PlayerTemplate(PlayerTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.player_name.text = self.item[0]
    self.board_color.background = self.item[1]
    self.pass_hand.text = self.item[2]