from django.conf.urls import patterns, include, url

from django.contrib import admin

from news import views
from DjangoUeditor import urls as DjangoUeditor_urls
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', views.column_detail),
    url(r'^news/(?P<article_slug>[^/]+)/$',  views.article_detail),

    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),

]

# use Django server /media/ files
from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
