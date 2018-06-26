# Create your views here.
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from web.models import *

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
