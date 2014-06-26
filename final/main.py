"""
Michael Saner
June 25 2014
Design Patterns for Web Programming
Final Project
"""
import webapp2
from urllib2 import urlopen
from json import load


#Controller class
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
            nv.nobjs = nm.objs
            p._body = nv.content

        #write everything to the page
        self.response.write(p.print_out())


#View class
class NewsView(object):
    ''' determines how data is displayed on the page '''
    def __init__(self):
        self.__nobj = []
        self.__content = '<br>'

    def update(self):
        #for every object in the array do this
        for obj in self.__nobjs:
            self.__content += "Title: " + obj.title + "<br>"
            self.__content += "Date: " + obj.date + "<br>"
            self.__content += "Lead-in: " + obj.teaser + "<br>"
            self.__content += "Read More: " + obj.link + "<br><br>"

    @property
    def content(self):
        return self.__content

    @property
    def nobjs(self):
        pass

    @nobjs.setter
    def nobjs(self, arr):
        self.__nobjs = arr
        self.update()


class NewsModel(object):
    ''' get, parse and sort data from the API '''
    def __init__(self):
        #this will access the api.
        self.__url = "http://api.npr.org/query?apiKey=MDE1MDY1ODMzMDE0MDM2NzY1NzAzYTJmOA001&numResults=5&format=json&id="
        #store user input here
        self.__id = ''
        #require stories pulled to have the following attributes
        self.__require = '&requiredAssets=text,image,audio'

    #send all the needed data to the api via url
    def callApi(self):
        response = urlopen(self.__url+self.__id+self.__require)
        json_obj = load(response)

        


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
