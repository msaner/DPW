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
        self.response.write('Hello world!')

class Food(object):
    def __init__(self):
        self.groceries = 0
        self.fast_food = 0
        self.dining_out = 0
        self.work_snacks = 0
        self.other = 0
        self.__total = 0 




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
