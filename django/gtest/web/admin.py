from django.contrib import admin
from web.models import Testcase
from django.utils import timezone
from django.contrib.admin.actions import delete_selected

# Register your models here.

def excute_case(modeladmin, request, queryset):
    queryset.update(last_use = timezone.now())
    count = queryset.get().use_count
    queryset.update(use_count = count + 1)
    case_path = queryset.get().test_case
    print(case_path)
    print(type(case_path))

excute_case.short_description = "执行测试用例"
delete_selected.short_description = '删除测试用例'


@admin.register(Testcase)
class TestcaseAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        """函数作用：使当前登录的用户只能看到自己负责的服务器"""
        qs = super(TestcaseAdmin, self).get_queryset(request)
        '''
        case_name = str(qs.get().test_case)
        if "/" in case_name: 
            case_name = case_name.split("/")[1]
        qs.update(test_case = case_name)
        '''
        if request.user.is_superuser:
            return qs
        return qs.filter(user_name = request.user)

    def changelist_view(self, request, extra_context = None):
        self.list_display = ['test_case', 'user_name', 'git_url', 
            'commit_id', 'create_time', 'last_use', 'use_count']
        if not request.user.is_superuser:
            self.list_display.remove("user_name")
        return super(TestcaseAdmin, self).changelist_view(request, extra_context = None)

    def save_model(self, request, obj, form, change):
        obj.user_name = request.user
        obj.save()

    def get_actions(self, request):
        actions = super(TestcaseAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

    fieldsets = (
        (u'测试用例信息',
            {'fields':
                ('git_url', 'commit_id', 'test_case')}),
    )
    add_fieldsets = (
        (u'测试用例信息',
            {'fields':
                ('git_url', 'user_name', 'commit_id', 'test_case')}),
    )
    search_fields = ('test_case', 'user_name')
    # list_filter = ('user_name',)
    ordering = ('-last_use',)
    actions = [excute_case]
    actions_on_top = True
    actions_selection_counter = True
    list_per_page = 5
    # list_editable = ('test_case', 'git_url', 'commit_id',)

admin.site.site_header = '规则自动化测试系统'
admin.site.site_title = 'Flow++测试系统'

