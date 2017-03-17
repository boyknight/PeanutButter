# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class RegisterHandler(tornado.web.RequestHandler):
    def post(self):
        self.write(self.request)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/register", RegisterHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()