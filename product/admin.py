from django.contrib import admin
from .models import *
from mptt.admin import DraggableMPTTAdmin
from django.utils.html import format_html
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)

class FilterAdmin(DraggableMPTTAdmin):
    # prepopulated_fields = {'slug': ('subcat',), }
    list_display = ('tree_actions', 'something')
    list_display_links = ('something',)

    def something(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.subcat,  # Or whatever you want to put here
        )
    something.short_description = ('Kateqoriya')

class SubCatgoryAdmin(admin.ModelAdmin):
    list_display= ('main_category','name')

class MarkaAdmin(admin.ModelAdmin):
    list_display= ('name',)


admin.site.register(Product,ProductAdmin)
admin.site.register(Filter,FilterAdmin)
admin.site.register(SubCategory,SubCatgoryAdmin)
admin.site.register(Marka,MarkaAdmin)