import json
import time

import tornado.web


from tornado.web import authenticated

from handlers import json_trans
from handlers import account

file="handlers/upload/file.json"


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        current_user = self.get_secure_cookie('ID')
        if current_user:
            return current_user
        return None

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        next = self.get_argument('next','')
        if next == '':
            self.render('Login.html',
                        nextname='login')
        else:
            self.render('Login.html',
                        nextname='login?next=' + next)
    def post(self, *args, **kwargs):
        nextname = self.get_argument('next','')
        username = self.get_argument('username',None)
        password = self.get_argument('password', None)
        if account.auth(username,password):
            self.set_secure_cookie('ID','user',expires=time.time()+30)

            if nextname == '':
                self.write('Welcome!!!'+username)
            else:
                self.redirect(nextname)
        else:
            self.write("用户名或者密码错误")


class ActionHandler(BaseHandler):

    '''
    Action加载页面
    '''

    @authenticated
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

class DomainHandler(BaseHandler):
    '''
    Action加载页面
    '''

    @authenticated
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