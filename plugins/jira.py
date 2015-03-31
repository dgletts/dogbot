from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class JiraTicket(WillPlugin):

    @hear("CS-(?P<ticket_number>.*?)$")
    def jira_ticket(self, message, ticket_number=None):
    	"""Convenient link: ______ """
    	formatted_jira_text = "Convenient link: https://util01.303net.net/jira/browse/CS-%(ticket_number)s" % {
    		"ticket_number": ticket_number,
    	}
    	self.say("Convenient link: https://util01.303net.net/jira/browse/CS-%(ticket_number)s" % locals(), message=message)

      