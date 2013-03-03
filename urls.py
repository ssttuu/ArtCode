from django.conf.urls.defaults import patterns, include, url

#from django.conf import settings
#from django.conf.urls.static import static

#from ArtCode.Page.views import RectangleList

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ArtCode.Page.views.home'),
    url(r'^posts/', include('ArtCode.Blog.urls')),
    url(r'^projects/', include('ArtCode.Blog.urls')),
    url(r'^about/', 'ArtCode.Page.views.about'),
    #url(r'^posts/', include('ArtCode.Page.urls')),
    # url(r'^ArtCode/', include('ArtCode.foo.urls')),

    #url(r'^rectangles/', RectangleList.as_view()),

    #url(r'^posts/', include('ArtCode.Blog.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment these two lines to enable your static files on PythonAnywhere
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

