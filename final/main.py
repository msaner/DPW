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
        #create the meta data for our form input
        p.inputs = [['id', 'text', 'Enter A Category ID'],['Submit', 'submit']]

        #if the user inters in a value execute...
        if self.request.GET:
            id = self.request.GET['id']
            #call the model
            nm = NewsModel()
            nm.id = self.request.GET['id']
            #connect to the api
            nm.callApi()

            #call view
            nv = NewsView()
            #get data from model and pass to the view
            nv.objs = nm.objs
            p._body = nv.content

        





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
