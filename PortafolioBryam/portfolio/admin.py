from django.contrib import admin
from .models import Project,Video
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass
admin.site.register(Video,MyModelAdmin)

class ProjectAdmin(AdminVideoMixin,admin.ModelAdmin):
    readonly_fields=('created','updated')
    pass

admin.site.register(Project,ProjectAdmin)
