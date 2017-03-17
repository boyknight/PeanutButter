# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.httputil

remote_ip = None

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if remote_ip is None:
            self.write("register first")
        else:
            self.redirect("http://{}".format(remote_ip))

class RegisterHandler(tornado.web.RequestHandler):

    def get(self):
        self.set_status(404)
        self.finish()

    def post(self):
        global remote_ip
        remote_ip = self.request.remote_ip
        self.write("Your IP: {}".format(remote_ip))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/register", RegisterHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()