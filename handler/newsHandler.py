__author__ = 'sam7'


import tornado.web


class NewsHandlelr(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")

    def post(self, *args, **kwargs):
        pass