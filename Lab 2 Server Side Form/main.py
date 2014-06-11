'''
Michael Saner
June 09, 2014
Design Patterns for Web Programming - Online
Simple Form
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

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_open = '''<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>DPWP-O Simple Form</title>

<link href='http://fonts.googleapis.com/css?family=Orbitron:500,700,900' rel='stylesheet' type='text/css'>
<link href='http://teamsaner.com/RMO/style.css' rel='stylesheet' type='text/css'>

</head>

<body>
<div class="container">
	<div class="screen">'''
    	page_form = '''<form method="GET" action="">
        	<label>First Name:</label><input type="text" name="first_name"><br>
            <label>Last Name:</label><input type="text" name="last_name"><br>
            <label>Email:</label><input type="text" name="email"><br>
            <label>Are you at least 18 years old?</label><br>
            <input type="radio" name="age" value="yes"> Yes
            <input type="radio" name="age" value="no"> No<br>
            <input type="checkbox" name="rules">  <span>I have read and agree to the official rules.</span><br>
        	<input type="submit" value="submit" class="button">
        </form>'''
        page_response = '''<p>Your Contest Entry...</p>

        '''
        page_close = '''</div>
</div>
</body>
</html>'''
        if self.request.GET:
            first_name = self.request.GET['first_name']
            last_name = self.request.GET['last_name']
            email = self.request.GET['email']
            age = self.request.GET['age']
            rules = self.request.GET['rules']
            if rules:
                rules = 'Yes'
            else:
                rules = 'No'

            self.response.write(page_open + 'The following information has been submitted to the contest, good luck!' + page_response + 'First Name: ' + first_name + '<br>' + 'Last Name: ' + last_name + '<br>' + 'Email: ' + email + '<br>' + 'Are you over 18?: ' + age + '<br>' + 'I agree to the contest rules: ' + rules + page_close)
        else:
            self.response.write(page_open + page_form + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
