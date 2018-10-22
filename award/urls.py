from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^new/post$',views.new_project, name='new-project'),
    url(r'votes/$',views.vote_project, name='vote_project'),
    url(r'^user/(\d+)$',views.detail, name='detail'),
    url(r'^detail/edit/$', views.edit_detail, name='edit-detail'),
    url(r'^search/$', views.search_results, name='search-user'),
    url(r'^comment/(?P<project_id>\d+)', views.add_comment, name='comment'),
    url(r'^vote/(?P<project_id>\d+)', views.vote, name='vote'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
