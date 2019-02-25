from django.contrib import admin

# Register your models here.
from booktest.models import Booktest, Hero
admin.site.register(Booktest)

#可以自定义模型管理类：
class HeroAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender', 'hmajor', 'hbook']
admin.site.register(Hero, HeroAdmin)

