"""
Michael Saner
June 25 2014
Design Patterns for Web Programming
Final Project
"""
import webapp2
from urllib2 import urlopen
from json import load


#Controller
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
