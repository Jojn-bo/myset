import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(111)
        u= self.get_argument('user')
        e= self.get_argument('email')
        p= self.get_argument('pwd')
        if u=='alex' and p=='123' and e == 'alex@126.com':
            self.write('ok')
        else:
            self.write("滚")
    def post(self, *args, **kwargs):
        print(111)
        u = self.get_argument('user')
        e = self.get_argument('email')
        p = self.get_argument('pwd')
        print(u, e, p)
        self.write('POST')
application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()