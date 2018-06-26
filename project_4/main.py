import os.path

import tornado.web
import tornado.options
from tornado.options import define,options

from handlers import handler

define('port',default=8000,help='run port',type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/action', handler.ActionHandler),
            (r'/domain', handler.DomainHandler),
            (r'/test', handler.TestHandler),
            (r'/login',handler.LoginHander)
        ]

        settings=dict(
            debug=True,
            template_path=os.path.join(os.path.dirname(__file__),'templates'),
            static_path =os.path.join(os.path.dirname(__file__), 'static'),
        )
        super(Application, self).__init__(handlers,**settings)


application=Application()


if __name__=='__main__':
    tornado.options.parse_command_line()
    print(options.port)
    http_server=tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.PollIOLoop.instance().start()