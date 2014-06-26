"""
Michael Saner
June 25 2014
Design Patterns for Web Programming
Final Project
"""
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
