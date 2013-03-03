from django.conf.urls.defaults import patterns, include, url

#from django.conf import settings
#from django.conf.urls.static import static

#from django.conf.urls import patterns, url
#from ArtCode.Page.views import RectangleList

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'(?P<postSlug>.*)', 'ArtCode.Page.views.post'),
    # url(r'^ArtCode/', include('ArtCode.foo.urls')),

    #url(r'^rectangles/', RectangleList.as_view()),


    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)

#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Uncomment these two lines to enable your static files on PythonAnywhere
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#urlpatterns += staticfiles_urlpatterns()

