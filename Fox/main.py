import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
#abstract class. this will hold our initial page HTML
        self._open = '''
        <!doctype html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title></title>
                <link href="http://www.teamsaner.com/RMO/main.css" rel="stylesheet" type="text/css">
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
        '''
        self._thumb = '''
                            <img src="">
                            <span></span>
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
        lion.sound = 'rawrrr'
        lion.pic = 'http://www.teamsaner.com/RMO/images/lion.png'

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
        zebra.sound = 'neighh'
        zebra.pic = 'http://www.teamsaner.com/RMO/images/zebra.png'

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
        elephant.sound = 'arooooomf'
        elephant.pic = 'http://www.teamsaner.com/RMO/images/elephant.png'

        #we need to store all these animals somewhere, lets make an array
        animals = [lion, zebra, elephant]

        #a function to write stuff to the apge
        if self.request.GET:
            #we're using i as an index to tell what animal to print info for but lets assign i and make it an int
            i = self.request.GET['i']
            i= int(i)
            #this variable will hold the current animal that's selected based on the link clicked
            #print the animal info out
            self.response.write(self._open + self._body + '<img src="http://www.teamsaner.com/RMO/images/' + str(animals[i].name) + '.png">'
                                                            '<span>' + str(animals[i].name) + '</span>' + '</div> <div id="info">' +
                                                            '<p>Phylum: ' + str(animals[i].phylum) + '</p>'
                                                            '<p>Class: ' + str(animals[i].a_class) + '</p>'
                                                            '<p>Order: ' + str(animals[i].order) + '</p>'
                                                            '<p>Family: ' + str(animals[i].family) + '</p>'
                                                            '<p>Genus: ' +  str(animals[i].genus) + '</p>'
                                                            '<p>Avg. Lifespan: ' + str(animals[i].life) + '</p>'
                                                            '<p>Habitat: ' +  str(animals[i].habitat) + '</p>'
                                                            '<p>Geo. Location: ' + str(animals[i].local) + '</p>' + self._close)
        #need to do something if nothing is clicked i.e. no animal is selected
        else:
            self.response.write(self._open + self._body + self._thumb + self._details + self._close)

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
        self.sound = 'animal noise'
        self.pic = ''

#drilling down to specific animals we will create sub classes that inherit the Animal super class
class Lion(Animal):
    def __init__(self):
        super(Lion, self).__init__()

class Zebra(Animal):
    def __init__(self):
        super(Zebra, self).__init__()

class Elephant(Animal):
    def __init__(self):
        super(Elephant, self).__init__()


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
