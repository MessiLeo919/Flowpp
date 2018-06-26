import json
import os
def json_transfer(file):
    with open(file,"r") as f:
        load_dict = json.load(f)         #转化为字典
        print(type(load_dict))    #转化为字典
        print("加载入文件完成...")
        print('----------------')
        List_date=[]
        List_date_1 = []
        List_date_2 = []
        List_date_3 = []
        for list_class in load_dict.keys():
            print(list_class)
            # List_class.append(list_class)     #获取四大类
            if list_class in ["action","service"]:
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
                if list_class =="action":
                    List_date_1.append(app_L_1)
                    List_date_1.append(dict_All_1)
                else:
                    List_date_2.append(app_L_1)
                    List_date_2.append(dict_All_1)

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
                        List_date_2.append(app_L_2)
                        List_date_2.append(dict_All_2)
    List_date=List_date_1+List_date_2+List_date_3

    return List_date


def json_modified(file,List_results):
    print("转换开始...")
    with open(file,"r") as f:
        load_dict = json.load(f)         #转化为字典

        print('----------------')
        with open("handlers/d.json", "w", encoding='utf-8') as fp:
            print("新建----------------")
            for list_class in load_dict.keys():
                # print(list_class)
                # List_class.append(list_class)     #获取四大类
                if list_class in ["action","service","application"]:
                    for i in load_dict[list_class]: #i为大类下面每一个字典
                        if i['name_cn'] in List_results:
                            i["selection"] = True
                        else:
                            i["selection"] = False
                            # i.update({"selection": false})
            json.dump(load_dict, fp, indent=4,ensure_ascii=False)
        print("转换完成")
