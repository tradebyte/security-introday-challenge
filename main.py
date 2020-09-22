import tornado.ioloop
import tornado.web

import os
from sys import exit
import sqlite3

connection = sqlite3.connect('db')
cursor = connection.cursor()

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        cursor.execute("SELECT * FROM fruits")
        x = cursor.fetchall()
        
        self.render("index.html", fruits=x)

    def post(self):
        feedback = self.get_argument('feedback')
        self.write("Thank you for the feedback: " + feedback)

class FruitHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self, id):
        cursor.execute("update fruits set quantity=" + self.get_argument("quantity") + " where id=" + id)
        connection.commit()

        self.redirect("/")

class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")
    
    def post(self):
        cursor.execute("SELECT * FROM users WHERE username=\"{}\" AND password=\"{}\"".format(self.get_body_argument('username'), self.get_body_argument("password")))
        a = cursor.fetchone()

        if not a:
            self.render("login.html")
            return

        self.set_secure_cookie("user", a[1])
        self.redirect("/")

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/fruit/(.*)", FruitHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogoutHandler),
        ]
        settings = {
            "template_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "templates"
            ),
            "static_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "static"
            ),
            "cookie_secret": "Chscf8wQI0rtYZBYE0Bx",
            "login_url": "/login",
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    app = Application()
    app.listen(8000)
    print(f"App running: http://localhost:8000")
    tornado.ioloop.IOLoop.current().start()
