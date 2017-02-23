from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from housing_backend import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^affordable/$', views.AffordableList.as_view()),
    url(r'^affordable/(?P<pk>[0-9]+)/$', views.AffordableDetail.as_view()),
    url(r'^rent/$', views.RentList.as_view()),
    url(r'^$', schema_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
