from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class Poppin(WillPlugin):

    @hear("^what(?: s|'s)? (?:up|poppin)")
    def poppin(self, message):
    	"""What's Poppin Dogbot?"""
    	self.say("Run the Jewels", message=message)

      