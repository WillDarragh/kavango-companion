from ._anvil_designer import MainTemplate
from anvil import *

from anvil.js.window import scrollTo

from About import About
from AnimalTable import AnimalTable
from Installing import Installing
from Randomizer import Randomizer

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def randomizer_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    scrollTo(0, 0)
    self.content_panel.add_component(Randomizer())

  def animal_table_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    scrollTo(0, 0)
    self.content_panel.add_component(AnimalTable())

  def rulebook_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def installing_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    scrollTo(0, 0)
    self.content_panel.add_component(Installing())

  def about_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    scrollTo(0, 0)
    self.content_panel.add_component(About())
