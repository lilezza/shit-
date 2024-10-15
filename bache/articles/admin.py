from django.contrib import admin
from.models import Articles
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

# Register your models here.


def published_fa(model):
    return datetime2jalali(model.published_at).strftime('%a, %d %b %Y %H:%M:%S')
published_fa.short_description = 'زمان انتشار'

@admin.register(Articles)
class ArticleAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ('title' , 'view' , published_fa , 'show')
    date_hierarchy = 'published_at'
    search_fields = ('title' ,)
    list_filter = ('published_at',)
    ordering = ['-published_at']
    actions = ['make_hide' , 'make_show']

    fieldsets = (
        (None, {
            'fields': ('title', 'body', 'published_at'),
        }),
        ('advance option', {
        "classes": ("collapse"),
        'fields': ('view', 'show'),
        })
    )

    class Media:
        js = ('admin/js/vendor/jquery/jquery.js', 'admin/js/jquery.init.js', 'admin/js/actions.js',)


    def make_hide(self , request , queryset):
        row_updated = queryset.update(show=0)
        self.giveMessage(request , row_updated , 'hide')

    make_hide.short_description = 'Make selected articles as hide'

    def make_show(self , request , queryset):
        row_updated = queryset.update(show=1)
        self.giveMessage(request , row_updated , 'show')

    make_show.short_description = "Make selected articles as show"

    def giveMessage(self, request , row_updated , type):
        if(row_updated == 1):
            message_bit = '1 article was'
        else:
            message_bit = "%s articles were" %row_updated

        self.message_user(request , "%s successfully marked as %s" % (message_bit , type))



# admin.site.register(Articles , ArticleAdmin)
