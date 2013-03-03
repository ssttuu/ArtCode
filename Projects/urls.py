from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('ArtCode.Projects.views',
    url(r'^$', 'index'),
    url(r'^(?P<project_name>[A-Za-z][A-Za-z0-9]+)/$', 'project'),
)