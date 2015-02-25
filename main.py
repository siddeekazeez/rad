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
from google.appengine.api import users
import webapp2
import jinja2
import os
import time
from google.appengine.api import mail

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')),
    extensions=['jinja2.ext.autoescape'])
    
    
class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url(self.request.path)
        timet = time.strftime("%I:%M %p")
        datet = time.strftime("%A, %d %B %Y")
        if user:
            template = JINJA_ENVIRONMENT.get_template('home.html')
            template_values = {
                'user': user.nickname(),
                'user_logout': logout_url,
                'url_logout_text': 'Log Out',
                'time': timet,
                'date': datet,
                'timelink': '/TimeSwitch',
                'emailmsg': "",
            }

            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
    def post(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url(self.request.path)
        timet = time.strftime("%I:%M %p")
        if user:
            template = JINJA_ENVIRONMENT.get_template('home.html')
            message = mail.EmailMessage()
            message.sender = user.email()
            message.to = "abdula17@uni.coventry.ac.uk"
            message.subject = "Comment Left on Weather App"
            message.body = """
                You have received a comment from %s,
                
                %s.
                            
                """ % (user, self.request.get('content'))

            message.send()
            email_message = 'Thank you for the comment'
            template_values = {
                'user': user.nickname(),
                'user_logout': logout_url,
                'url_logout_text': 'Log Out',
                'time': timet,
                'timelink': '/TimeSwitch',
                'emailmsg': email_message,
            }

            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
    
class TimeSwitch(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url(self.request.path)
        timet = time.strftime("%H:%M")
        if user:
            template = JINJA_ENVIRONMENT.get_template('home.html')
            template_values = {
                'user': user.nickname(),
                'url_logout': logout_url,
                'url_logout_text': 'Log out',
                'time': timet,
                'timelink': '/',

            }
            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/TimeSwitch', TimeSwitch),
], debug=True)
