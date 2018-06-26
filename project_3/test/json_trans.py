import json

List_results=['微信_表情_接收']
print("转换开始...")
with open("test.json","r") as f:
    print("打开----------------")
    load_dict = json.load(f)
    print(type(f))
    print(type(load_dict))
    with open("d.json","w",encoding='utf-8') as fp:
        print("新建----------------")
        for list_class in load_dict.keys():
            if list_class in ["action","service","application"]:
                for i in load_dict[list_class]:
                    if i['name_cn'] in List_results:
                        i["selection"] = True
                    else:
                        i["selection"] = False
        # print(type(load_dict))
        # print(load_dict)
        # load=json.dumps(load_dict)
        # print(type(load))
        # print("--------------")
        json.dump(load_dict,fp,ensure_ascii=False)
    print("转换完成")
