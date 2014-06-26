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
        p = FormPage()
        #input form array
        p.inputs = [['id', 'text', 'Enter A Category ID'], ['Submit', 'submit']]

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
        self.__content = '<hr>'

    def update(self):
        #for every object in the array do this
        for obj in self.__nobjs:
            self.__content += "<h2>" + obj.title + "</h2>"
            self.__content += "<p>" + obj.teaser + "</p>"
            self.__content += '<a href="' + obj.link + '" target="_blank">Read This Article</a>'

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

        self._objs = []
        #create the following data objects and store them in the objs array
        for story in json_obj['list']['story']:
            obj = NewsData()
            obj.title = story['title']['$text']
            obj.teaser = story['teaser']['$text']
            obj.link = story['link'][0]['$text']

            self._objs.append(obj)

    @property
    def objs(self):
        return self._objs

    @property
    def id(self):
        pass

    @id.setter
    def id(self, z):
        self.__id = z

class NewsData(object):
    ''' do something with the data we get from the model & shown in view '''
    def __init__(self):
        self.title = ''
        self.date = ''
        self.teaser = ''
        self.link = ''

#abstract class
class Page(object):
    def __init__(self):
        self._head = '''
        <!DOCTYPE HTML>
        <html>
            <head>
                <title></title>
                <link href="http://www.teamsaner.com/RMO/main.css" rel="stylesheet" type="text/css">
            </head>
            <body>
                <div id="container">
                    <h1>NPR Newsfeed Widget</h1>
                    <p>To customize your feed type in the ID for one of the following categories:</p>
                    <ul>
                        <li>Main news articles, enter: <span>1001</span></li>
                        <li>NPR homepage articles, enter: <span>1002</span></li>
                        <li>Movie articles, enter: <span>1045</span></li>
                        <li>Science articles, enter: <span>1007</span></li>
                        <li>Economic articles, enter: <span>1032</span></li>
                    </ul>

        '''
        self._body = ''
        self._close = '''
        </div>
            </div>
            </body>
        </html>'''

    def print_out(self):
        return self._head + self._body + self._close


#inheriting from class page
class FormPage(Page):
    def __init__(self):
        #constructor for super class
        super(FormPage, self).__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, array):
        self.__inputs = array
        #sort the array and add to input
        for item in array:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            #if there's another attribute add that too
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            #else just close the tag
            except:
                self._form_inputs += '" />'

    def print_out(self):
        return self._head + self._form_open + self._form_inputs + self._form_close + self._body + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
