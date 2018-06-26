import json
def json_transfer(file):
    with open(file,"r") as f:
        load_dict = json.load(f)         #转化为字典
        print("加载入文件完成...")
        print('----------------')

        # List_class=[]
        for list_class in load_dict.keys():
            # List_class.append(list_class)     #获取四大类
            if list_class =="action":
                app_L_1 = []
                dict_All_1 = []
                for i in load_dict[list_class]: #i为大类下面每一个字典
                    a=i['name_cn'].split("_")[0]

                    if a not in app_L_1:
                        app_L_1.append(a)
                        dict_name={a:[i['name_cn']]}
                        dict_All_1.append(dict_name)
                    else:
                        dict_All_1[app_L_1.index(a)][a].append(i['name_cn'])
            elif list_class =="application":
                app_L_2 = []
                dict_All_2 = []
                for i in load_dict[list_class]: #i为大类下面每一个字典
                    b = i['domain']
                    if b not in app_L_2:
                        app_L_2.append(b)
                        dict_name = {b: [i['name_cn']]}
                        dict_All_2.append(dict_name)
                    else:
                        dict_All_2[app_L_2.index(b)][b].append(i['name_cn'])



    return [app_L_1,dict_All_1,app_L_2,dict_All_2]
