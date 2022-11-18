from django.contrib import admin

# Register your models here.
from .models import Project, Report, Slideshow, Comment, Gallery

admin.site.site_header = "Greening Earth Administration"
admin.site.site_title = "Greening Earth Administration"
admin.site.index_title = "Welcome to Greening Earth admin site"
# Register your models here.



admin.site.register(Project)
admin.site.register(Report)
admin.site.register(Slideshow)
admin.site.register(Comment)
admin.site.register(Gallery)
