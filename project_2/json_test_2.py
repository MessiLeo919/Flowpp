import json
def json_transfer(file):
    with open(file,"r") as f:
        load_dict = json.load(f)         #转化为字典
        print("加载入文件完成...")
        print('----------------')

        m=0
        List_class=[]
        dict_app_1={}
        dict_app_2={}
        for list_class in load_dict.keys():
            List_class.append(list_class)     #获取四大类

        # print(load_dict['service'])
        #     app_list= []
        #     m+=1
            action_app = []

            if list_class =="action":
                app_L_1 = []
                dict_All = []
                for i in load_dict[list_class]:
                    a=i['name_cn'].split("_")[0]

                    if a not in app_L_1:
                        app_L_1.append(a)
                        dict_name={a:[i['name_cn']]}
                        dict_All.append(dict_name)
                    else:
                        dict_All[app_L_1.index(a)][a].append(i['name_cn'])

                print(dict_All)

                # print(action_app)
                print(app_L_1)
                # for i in load_dict[list_class]:
                #     i

                # for i in load_dict[list_class]:
                #     action_app.append(i['name_cn'])
                #     # a = i['name_cn'].split("_")[0]
                    # if a not in app_L_1:
                    #     app_L_1.append(a)
                #

            #
            # dict_app_1[list_class]=app_L_1

                # app_list.append(i['name_cn'])
        #     dict_app_1[list_class]=app_list
        #
        # print("有{}个类，分别如下{}：".format(m,List_class))
        # print(type(dict_app_1))
        # print(dict_app_1)

json_transfer("meta.json")

