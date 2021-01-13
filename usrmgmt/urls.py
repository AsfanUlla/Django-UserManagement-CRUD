from django.conf.urls import url 
from usrmgmt import views 
 
urlpatterns = [ 
    url(r'^api/users$', views.user_list),
    url(r'^api/users/(?P<pk>[0-9]+)$', views.user_edit),
    url(r'^api/csv$', views.gen_csv)
]