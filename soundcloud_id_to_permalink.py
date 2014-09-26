import webapp2
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch
import json as simplejson
try:
    import config
except ImportError:
    import config_template as config

class Handler(webapp2.RequestHandler):

    def get(self):
        id = self.request.get('id')
        response = urlfetch.fetch('https://api.soundcloud.com/tracks/' + id + '.json?consumer_key=' + config.SOUNDCLOUD_CONSUMER_KEY)
        json = simplejson.loads(response.content)
        self.redirect(str(json['permalink_url']))

app = webapp2.WSGIApplication([
        ('/soundcloud_id_to_permalink', Handler),
    ], debug=False)
