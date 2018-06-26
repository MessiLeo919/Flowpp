import tornado.web
import json
# import requests

from handlers import json_trans

a=json_trans.json_transfer("handlers/atest.json")



class ActionHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('Action.html',
                    app_L_1=a[0],
                    dict_All_1=a[1],
                    )
    def post(self, *args, **kwargs):

        result = tornado.escape.json_decode(self.request.body)
        print("result:", result)
        print(type(result))
        json_trans.json_modified("handlers/atest.json",result)
        print("数据提交成功！")
        self.render('test.html')




class DomainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello")
        self.render('Domain.html',
                    app_L_2=a[2],
                    dict_All_2=a[3],
                    app_L_3=a[4],
                    dict_All_3=a[5]
                    )


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("数据提交完成")