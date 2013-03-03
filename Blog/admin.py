from ArtCode.Blog.models import Category,Post,Picture,Visualization
from django.contrib import admin

admin.site.register( Category)
admin.site.register( Picture)
admin.site.register( Visualization)
admin.site.register( Post)