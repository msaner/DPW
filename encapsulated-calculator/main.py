'''
Michael Saner
June 10, 2014
Design Patterns for Web Programming - Online
Encapsulated Calculator
'''

# !/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from pages import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #weekly expenses for users

        #Robert
        r = write_stuff()
        r.groceries = 90
        r.fast_food = 40
        r.dining_out = 40
        r.work_snacks = 5
        r.other = 0
        #call the getter function and print result
        r.total = int(r.groceries) + int(r.fast_food) + int(r.dining_out) + int(r.work_snacks) + int(r.other)
        r.update()

        #Mary
        m = write_stuff()
        m.groceries = 55
        m.fast_food = 23
        m.dining_out = 81
        m.work_snacks = 7
        m.other = 14

        m.total = m.groceries + m.fast_food + m.dining_out + m.work_snacks + m.other
        m.update()

        #James
        j = write_stuff()
        j.groceries = 213
        j.fast_food = 57
        j.dining_out = 0
        j.work_snacks = 13
        j.other = 21

        j.total = j.groceries + j.fast_food + j.dining_out + j.work_snacks + j.other
        j.update()

        #Katy
        k = write_stuff()
        k.groceries = 118
        k.fast_food = 56
        k.dining_out = 21
        k.work_snacks = 4
        k.other = 0

        k.total = k.groceries + k.fast_food + k.dining_out + k.work_snacks + k.other
        k.update()

        #Steve
        s = write_stuff()
        s.groceries = 249
        s.fast_food = 87
        s.dining_out = 107
        s.work_snacks = 36
        s.other = 0

        s.total = s.groceries + s.fast_food + s.dining_out + s.work_snacks + s.other
        s.update()


    #the HTML
class write_stuff(object):
    def __init__(self):
        # these attributes will be public unless noted otherwise
        self.groceries = 0
        self.fast_food = 0
        self.dining_out = 0
        self.work_snacks = 0
        self.other = 0
        self.__total = 0  # the total attribute is private


        #this here is the template
        self.page = '''<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Food Cost Calculator</title>


        <link href="http://www.teamsaner.com/RMO/main.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        '''
        self.body = '''<div class="container">

    	<h1>Weekly Food Cost Calculator</h1>
        <p>Click on a users name to reveal their weekly expenses.</p>
    <div class="chart">
		<form action="" method="GET" name="expenses" id="user-spending">
        	<input type="submit" value="Robert" name="process" class="button"><br>
            <input type="submit" value="Mary" name="process" class="button"><br>
			<input type="submit" value="James" name="process" class="button"><br>
			<input type="submit" value="Katy" name="process" class="button"><br>
			<input type="submit" value="Steve" name="process" class="button">
        </form>

        <div>
        	<a href="?user=r">Robert</a>
            <a href="?user=m">Mary</a>
            <a href="?user=j">James</a>
            <a href="?user=k">Katy</a>
            <a href="?user=s">Steve</a>
        </div>
     </div><!-- chart -->

    <div class="receipt">
    	<img src="http://www.teamsaner.com/RMO/receipt.jpg">
        <div class="total">
        	<p>Groceries: ${self.groceries}</p>
            <p>Fast Food: ${self.fast_food}</p>
        	<p>Dining Out: ${self.dining_out}</p>
            <p>Work Snacks: ${self.work_snacks}</p>
            <p>Other: ${self.other}</p>
        </div>
    </div>
        '''
        self.close = '''
    </body>
</html>
        '''
    def update(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())


    #set up a getter so we can use the private data
    @property
    def total(self):  #make sure this function name matches the attribute above
        #calculate the weekly cost of food
        self.__total
        return self.__total

    #setter this won't be used in this application right now
    @total.setter
    def total(self):
        pass

# can't touch this nah na na nahh... can't touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
