# Create your views here.
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from web.models import *


import json
import os
# Create your views here.
class TestcaseForm(forms.Form):
    #form的定义和model类的定义很像
    git_url     = forms.CharField()
    commit_id   = forms.CharField()
    user_name   = forms.CharField()
    test_case   = forms.FileField()
    create_time = forms.DateField()
    last_use    = forms.DateField()
    use_count   = forms.IntegerField()

#在View中使用已定义的Form方法
def registerTestcase(request):
    #刚显示时调用GET方法
    if request.method=="POST":
        uf = TestcaseForm(request.POST,request.FILES)#刚显示时，实例化表单（是否有数据）
        logging.info(request.user)
        if uf.is_valid():#验证数据是否合法，当合法时可以使用cleaned_data属性。
            #用来得到经过'clean'格式化的数据，会所提交过来的数据转化成合适的Python的类型。
            git_url     = uf.cleaned_data['git_url']
            commit_id   = uf.cleaned_data['commit_id']
            user_name   = uf.cleaned_data['user_name']
            test_case   = uf.cleaned_data['test_case']
            create_time = uf.cleaned_data['create_time']
            last_use    = uf.cleaned_data['last_use']
            use_count   = uf.cleaned_data['use_count']
            #write in database
            ts = Testcase()#实例化NormalUser对象
            ts.git_url     = git_url
            ts.commit_id   = commit_id
            ts.user_name   = request.user.username
            ts.test_case   = test_case
            ts.cerate_time = create_time
            ts.last_use    = last_use
            ts.use_count   = use_count
            ts.save()#保存到数据库表中
            return HttpResponse('Upload Succeed!')#重定向显示内容（跳转后内容）
    else:
        uf=TestcaseForm()#刚显示时，实例化空表单
    return render(request,'register.html',{'uf':uf})#只有刚显示时才起作用

file="web/meta.json"
def json_transfer(file):
    print("加载中...",file)
    with open(file,"r") as f:
        load_dict = json.load(f)         #转化为字典
        print("加载文件完成...")
        List_date_1 = []
        List_date_2 = []
        List_date_3 = []
        for list_class in load_dict.keys():
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
                    # print(i)
                    b = i['domain']
                    # print(b)
                    if b not in app_L_2:
                        app_L_2.append(b)
                        dict_name = {b: [i['name_cn']]}
                        dict_All_2.append(dict_name)
                    else:
                        dict_All_2[app_L_2.index(b)][b].append(i['name_cn'])
                List_date_3.append(app_L_2)
                List_date_3.append(dict_All_2)


    List_date=List_date_1+List_date_2+List_date_3
    return List_date
    # except FileNotFoundError:
    #     return [[],[],[],[],[],[]]

def json_modified(file,List_results):
    print("转换开始...")
    with open(file,"r") as f:
        load_dict = json.load(f)         #转化为字典
        with open("web/new_json_file/new_meta.json", "w", encoding='utf-8') as fp:
            print("新建...")
            for list_class in load_dict.keys():#获取四大类
                if list_class in ["action","service","application"]:
                    for i in load_dict[list_class]: #i为大类下面每一个字典
                        if i['name_cn'] in List_results:
                            i["selection"] = True
                else:
                            i["selection"] = False
            json.dump(load_dict, fp, indent=4,ensure_ascii=False)


        print("转换完成")




def index(request):
    return render(request,"aaction.html")
def test(request):
    return HttpResponse("aaction.html")
def action(request):
    if request.method == 'GET':
        parameter = json_transfer(file)
        return render(request,'Action.html',
                    context={
                        'app_L_1' :parameter[0],
                        'dict_All_1' : parameter[1],

                    }
        )
    elif request.method == 'POST':
        result =json.loads(request.body)
        print(result)
        json_modified(file, result)
        print("数据提交成功！")
        return render(request,'Finish.html')


def Domain(request):
    if request.method == 'GET':
        parameter = json_transfer(file)
        return render(request,'Domain.html',
                      context={
                          'app_L_2':parameter[4],
                          'dict_All_2': parameter[5],
                          'app_L_3': parameter[2],
                          'dict_All_3': parameter[3]
                      }
                    )
    elif request.method == 'POST':
        result = json.loads(request.body)
        print(result)
        json_modified(file, result)
        print("数据提交成功！")
        return render(request, 'Finish.html')

def Finish(request):
    if request.method == 'GET':
        return render(request,'Finish.html',)