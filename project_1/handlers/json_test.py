import json
def json_transfer(file):
    with open(file,"r") as f:
        load_dict = json.load(f)
        print("加载入文件完成...")
        print('----------------')

        app_obj=[]# 所有具体名单
        m=0
        app_class=[]
        dict_app={}
        for app_kinds in load_dict.keys():
            app_class.append(app_kinds)
            app_list= []
            m+=1
            for i in load_dict[app_kinds]:
                app_list.append(i['name_cn'])
            dict_app[app_kinds]=app_list
        print("有{}个类，分别如下{}：".format(m,app_class))
        print(dict_app)

        # for j in dict_app[i]:
        #     print(j)



json_transfer("../conf.json")

