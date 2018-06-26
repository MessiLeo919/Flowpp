import tornado.web
import json

from handlers import json_trans





class LoginHander(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('Login.html')
    def post(self, *args, **kwargs):
        json_files = self.request.files.get('json_file',None)
        print(type(json_files))
        for json_file in json_files:
            print(json_file['filename'])
            with open('./handlers/upload/file.json','wb') as f:
                f.write(json_file['body'])

        self.redirect('action')
        # self.write("上传文件成功！")

class ActionHandler(tornado.web.RequestHandler):

    def get(self):
        # print(self.get_argument('data'))
        # print(a)
        a = json_trans.json_transfer("handlers/upload/file.json")
        self.render('Action.html',
                    app_L_1=a[0],
                    dict_All_1=a[1],
                    )
    def post(self, *args, **kwargs):
        # print(self.request.body)
        result = tornado.escape.json_decode(self.request.body)
        print(type(result))
        print("result:", result)

        json_trans.json_modified("handlers/upload/file.json",result)
        print("数据提交成功！")
        self.render('test.html')




class DomainHandler(tornado.web.RequestHandler):
    def get(self):
        a = json_trans.json_transfer("handlers/upload/file.json")
        # self.write("Hello")
        self.render('Domain.html',
                    app_L_2=a[4],
                    dict_All_2=a[5],
                    app_L_3=a[2],
                    dict_All_3=a[3]
                    )
    def post(self, *args, **kwargs):
        result = tornado.escape.json_decode(self.request.body)
        print(type(result))
        print("result:", result)
        json_trans.json_modified("handlers/upload/file.json",result)
        print("数据提交成功！")
        self.render('test.html')


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        # self.render('test.html')
        self.write("转换完成！")