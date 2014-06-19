import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()


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
        self._details = '''
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
#add animal information
        #call the lion subclass to run
        lion = Lion()
        lion.name = ''
        lion.phylum = ''
        lion.a_class = ''
        lion.order = ''
        lion.family = ''
        lion.genus = ''
        lion.life = ''
        lion.habitat = ''
        lion.local = ''
        lion.sound = ''

        #call the zebra subclass to run
        zebra = Zebra()
        zebra.name = ''
        zebra.phylum = ''
        zebra.a_class = ''
        zebra.order = ''
        zebra.family = ''
        zebra.genus = ''
        zebra.life = ''
        zebra.habitat = ''
        zebra.local = ''
        zebra.sound = ''

        #call the lion subclass to run
        lion = Lion()
        lion.name = ''
        lion.phylum = ''
        lion.a_class = ''
        lion.order = ''
        lion.family = ''
        lion.genus = ''
        lion.life = ''
        lion.habitat = ''
        lion.local = ''
        lion.sound = ''




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
