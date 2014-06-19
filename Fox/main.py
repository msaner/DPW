import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write('Hello world!')


#abstract class. this will hold our initial page HTML
class Page(object):
    def __init__(self):
        self._open = '''
        <!doctype html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title></title>
                <link href="main.css" rel="stylesheet" type="text/css">
            </head>
        '''
        self._body = '''
            <body>
                <div id="container">
                    <nav>
                        <a href="?i=0">Lion</a>
                        <a href="?i=1">Zebra</a>
                        <a href="?i=2">Elephant</a>
                    </nav>
                    <div id="card">
                        <div id="animal">
                            <img src="images/lion.png">
                            <span>Lion</span>
                        </div>
                        <div id="info">
        '''
        self._close = '''
                            <p>Phylum:</p>
                            <p>Class: </p>
                            <p>Order: </p>
                            <p>Family: </p>
                            <p>Genus: </p>
                            <p>Avg. Lifespan</p>
                            <p>Habitat: </p>
                            <p>Geo. Location</p>
        '''
        self._close = '''
                        </div>
                    </div>
                </div>
            </body>
        </html>
        '''




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
