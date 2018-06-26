<<<<<<< HEAD
import tornado
=======
import tornado.web
>>>>>>> 57eaf1354c3e094c2bac42669da45d66725c8424
import json

with open("meta.json", "r") as f:
    load_dict = json.load(f)
    print("加载入文件完成...")
    print('----------------')

    app_obj = []  # 所有具体名单
    m = 0
    app_class = []
    dict_app = {}
    for app_kinds in load_dict.keys():
        app_class.append(app_kinds)
        app_list = []
        m += 1
        for i in load_dict[app_kinds]:
            app_list.append(i['name_cn'])
        dict_app[app_kinds] = app_list
    print("有{}个类，分别如下{}：".format(m, app_class))
    print(dict_app)

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('base_2.html',
                    app_class=app_class,
                    dict_app=dict_app,
                    )
    def post(self, *args, **kwargs):
        account = self.get_arguments('action')
        print("action:",account)
        account = self.get_arguments('app')
        print("app:",account)
        account = self.get_arguments('service')
        print("service:",account)
        account = self.get_arguments('domain')
        print("domain:",account)
        # print(type(account))
        self.write("数据提交成功！")
