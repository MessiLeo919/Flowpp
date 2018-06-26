import tornado.web
import json
import time

from handlers import json_trans

file="handlers/upload/file.json"
class ActionHandler(tornado.web.RequestHandler):

    '''
    Action加载页面
    '''

    def get(self, *args, **kwargs):
            parameter = json_trans.json_transfer(file)
            self.render('Action.html',
                        app_L_1=parameter[0],
                        dict_All_1=parameter[1],
                        )

    def post(self, *args, **kwargs):

        json_files = self.request.files.get('json_file', None)
        if json_files:
            for json_file in json_files:
                with open('./handlers/upload/file.json', 'wb') as f:
                    f.write(json_file['body'])
            self.redirect('action')
        else:
            try:
                result = tornado.escape.json_decode(self.request.body)
            except json.decoder.JSONDecodeError:
                self.redirect('action')
                return

            try:
                json_trans.json_modified("handlers/upload/file.json", result)
                print("数据提交成功！")
                self.render('Finish.html')
            except FileNotFoundError:
                print("-----------------文件没找到")

class DomainHandler(tornado.web.RequestHandler):
    '''
    Action加载页面
    '''

    def get(self):
        parameter = json_trans.json_transfer(file)
        self.render('Domain.html',
                    app_L_2=parameter[4],
                    dict_All_2=parameter[5],
                    app_L_3=parameter[2],
                    dict_All_3=parameter[3]
                    )
    def post(self, *args, **kwargs):

        result = tornado.escape.json_decode(self.request.body)
        try:
            json_trans.json_modified("handlers/upload/file.json",result)
            print("数据提交成功！")
            self.render('Finish.html')
        except FileNotFoundError:
            print("-----------------文件没找到")

class FinishHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("转换完成！")