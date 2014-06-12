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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #weekly expenses for users

        #Robert
        r = Food()
        r.groceries = 90
        r.fast_food = 40
        r.dining_out = 40
        r.work_snacks = 5
        r.other = 0

        #Mary
        m = Food()
        m.groceries = 55
        m.fast_food = 23
        m.dining_out = 81
        m.work_snacks = 7
        m.other = 14

        #James
        j = Food()
        j.groceries = 213
        j.fast_food = 57
        j.dining_out = 0
        j.work_snacks = 13
        j.other = 21

        #Katy
        s = Food()
        s.groceries = 55
        s.fast_food = 23
        s.dining_out = 81
        s.work_snacks = 7
        s.other = 14

        #Steve
        s = Food()
        s.groceries = 55
        s.fast_food = 23
        s.dining_out = 81
        s.work_snacks = 7
        s.other = 14




class Food(object):
    def __init__(self):
        # these attributes will be public unless noted otherwise
        self.groceries = 0
        self.fast_food = 0
        self.dining_out = 0
        self.work_snacks = 0
        self.other = 0
        self.__total = 0 # the total attribute is private



# can't touch this nah na na nahh... can't touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
