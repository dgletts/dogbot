import random
import requests
from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class MainScreenPlugin(WillPlugin):

    @respond_to("main screen on")
    def main_screen(self, message):
        """request denied"""
        data = {
            "q": "no",
            "v": "1.0",
            "safe": "active",
            "rsz": "8"
        }
        r = requests.get("http://ajax.googleapis.com/ajax/services/search/images", params=data)
        try:
            results = r.json()["responseData"]["results"]
        except TypeError:
            results = []
        if len(results) > 0:
            url = random.choice(results)["unescapedUrl"]
            self.say("%s" % url, message=message)
        else:
            self.say("Couldn't find anything!", message=message)