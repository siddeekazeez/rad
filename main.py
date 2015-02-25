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
                'datelink': '/DateSwitch',
                'emailmsg': "",
            }

            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
    def post(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url(self.request.path)
        timet = time.strftime("%I:%M %p")
        datet = time.strftime("%A, %d %B %Y")
        if user:
            template = JINJA_ENVIRONMENT.get_template('home2.html')
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
                'date': datet,
                'timelink': '/TimeSwitch',
                'datelink': '/DateSwitch',
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
        datet = time.strftime("%A, %d %B %Y")
        if user:
            template = JINJA_ENVIRONMENT.get_template('home.html')
            template_values = {
                'user': user.nickname(),
                'url_logout': logout_url,
                'url_logout_text': 'Log out',
                'time': timet,
                'date': datet,
                'timelink': '/',
                'datelink': '/DateTimeSwitch',
            }
            
            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
    def post(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url(self.request.path)
        timet = time.strftime("%H:%M")
        datet = time.strftime("%A, %d %B %Y")
        if user:
            template = JINJA_ENVIRONMENT.get_template('home2.html')
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
                'date': datet,
                'timelink': '/',
                'datelink': '/DateTimeSwitch',
                'emailmsg': email_message,
            }

            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            

class DateSwitch(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url(self.request.path)
        timet = time.strftime("%I:%M %p")
        datet = time.strftime("%d/%m/%Y")
        if user:
            template = JINJA_ENVIRONMENT.get_template('home.html')
            template_values = {
                'user': user.nickname(),
                'url_logout': logout_url,
                'url_logout_text': 'Log out',
                'time': timet,
                'date': datet,
                'timelink': '/DateTimeSwitch',
                'datelink': '/',

            }
            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
    def post(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url(self.request.path)
        timet = time.strftime("%I:%M %p")
        datet = time.strftime("%d/%m/%Y")
        if user:
            template = JINJA_ENVIRONMENT.get_template('home2.html')
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
                'date': datet,
                'timelink': '/DateTimeSwitch',
                'datelink': '/',
                'emailmsg': email_message,
            }

            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
            
class DateTimeSwitch(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url(self.request.path)
        timet = time.strftime("%H:%M")
        datet = time.strftime("%d/%m/%Y")
        if user:
            template = JINJA_ENVIRONMENT.get_template('home.html')
            template_values = {
                'user': user.nickname(),
                'url_logout': logout_url,
                'url_logout_text': 'Log out',
                'time': timet,
                'date': datet,
                'timelink': '/DateSwitch',
                'datelink': '/TimeSwitch',

            }
            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
    def post(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url(self.request.path)
        timet = time.strftime("%H:%M")
        datet = time.strftime("%d/%m/%Y")
        if user:
            template = JINJA_ENVIRONMENT.get_template('home2.html')
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
                'date': datet,
                'timelink': '/DateSwitch',
                'datelink': '/TimeSwitch',
                'emailmsg': email_message,
            }

            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/TimeSwitch', TimeSwitch),
    ('/DateSwitch', DateSwitch),
    ('/DateTimeSwitch', DateTimeSwitch),
], debug=True)
