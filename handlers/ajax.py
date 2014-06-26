#conding=utf-8

import tornado.web

class AjaxHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('ajax_form.html')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")

        self.write(username + password)
