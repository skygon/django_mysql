from django.urls import path

from . import response

# info/list?page=<int:pageId>
# info/<int:projectId>
urlpatterns = [
    #path('', views.index, name='index'),
    path('list/', response.get_all),
    path('<int:projectId>/', response.get_specific),
]
