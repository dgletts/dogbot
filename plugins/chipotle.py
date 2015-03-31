from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class Chipotle(WillPlugin):

    @hear("^chipotle")
    def chipotle(self, message):
    	"""Luh"""
    	self.say("I'm in LUHHHHHHH wit CHIPOTLE", message=message)

      