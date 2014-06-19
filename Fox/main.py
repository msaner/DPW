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
                            <p>Phylum: </p>
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
        lion.name = 'Lion'
        lion.phylum = 'Chordata'
        lion.a_class = 'Mammalia'
        lion.order = 'Carnivora'
        lion.family = 'Felidae'
        lion.genus = 'Panthera'
        lion.life = '10-14 years'
        lion.habitat = 'Jungle'
        lion.local = 'Africa'
        lion.sound = 'roarr'
        lion.pic = 'images/lion.png'

        #call the zebra subclass to run
        zebra = Zebra()
        zebra.name = 'Zebra'
        zebra.phylum = 'Chordata'
        zebra.a_class = 'Mammalia'
        zebra.order = 'Perissodactyla'
        zebra.family = 'Equidae'
        zebra.genus = 'Equus'
        zebra.life = '20-25 years'
        zebra.habitat = 'Plains'
        zebra.local = 'Africa'
        zebra.sound = 'nay snort'
        zebra.pic = 'images/zebra.png'

        #call the elephant subclass to run
        elephant = Elephant()
        elephant.name = 'Elephant'
        elephant.phylum = 'Chordata'
        elephant.a_class = 'Mammal'
        elephant.order = 'Proboscidea'
        elephant.family = 'Elephantidae'
        elephant.genus = 'Loxodonta'
        elephant.life = '60-70 years'
        elephant.habitat = 'Jungle, Plains'
        elephant.local = 'Africa'
        elephant.sound = 'oooompht'
        elephant.pic = 'images/elephant.png'

        #we need to store all these animals somewhere, lets make an array
        animals = [lion, zebra, elephant]
        #we're using i as an index to tell what animal to print info for but lets assign i and make it an int
        i = self.request.GET['i']
        i= int(i)
        #this variable will hold the current animal that's selected based on the link clicked
        animal = self.request.GET(animals[i].name)
        print animal.name

#create an animal super class
class Animal(object):
    def __init__(self):
        self.name = ''
        self.phylum = ''
        self.a_class = ''
        self.order = ''
        self.family = ''
        self.genus = ''
        self.life = ''
        self.habitat = ''
        self.local = ''
        self.sound = ''
        self.pic = ''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
