'''
Michael Saner
June 10, 2014
Design Patterns for Web Programming - Online
Encapsulated Calculator
'''

#!/usr/bin/env python
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
        p = Page()
        self.response.write(p.print_out())

        #weekly expenses for users

        #Robert
        r = Food()
        r.groceries = 90
        r.fast_food = 40
        r.dining_out = 40
        r.work_snacks = 5
        r.other = 0
        #call the getter function and print result
        self.response.write('Robert spent $' + str(r.total) + ' on food this week.')


        #Mary
        m = Food()
        m.groceries = 55
        m.fast_food = 23
        m.dining_out = 81
        m.work_snacks = 7
        m.other = 14
        self.response.write('Mary spent $' + str(m.total) + ' on food this week.')

        #James
        j = Food()
        j.groceries = 213
        j.fast_food = 57
        j.dining_out = 0
        j.work_snacks = 13
        j.other = 21
        self.response.write('James spent $' + str(j.total) + ' on food this week.')

        #Katy
        k = Food()
        k.groceries = 118
        k.fast_food = 56
        k.dining_out = 21
        k.work_snacks = 4
        k.other = 0
        self.response.write('Katy spent $' + str(k.total) + ' on food this week.')

        #Steve
        s = Food()
        s.groceries = 249
        s.fast_food = 87
        s.dining_out = 107
        s.work_snacks = 36
        s.other = 0
        self.response.write('Steve spent $' + str(s.total) + ' on food this week.')




class Food(object):
    def __init__(self):
        # these attributes will be public unless noted otherwise
        self.groceries = 0
        self.fast_food = 0
        self.dining_out = 0
        self.work_snacks = 0
        self.other = 0
        self.__total = 0 # the total attribute is private

    #set up a getter so we can use the private data
    @property
    def total(self): #make sure this function name matches the attribute above
        #calculate the weekly cost of food
        self.__total = self.groceries + self.fast_food + self.dining_out + self.work_snacks + self.other
        return self.__total

    #setter this won't be used in this application right now
    @total.setter
    def total(self):
        pass

# can't touch this nah na na nahh... can't touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
