from django.conf.urls import url
from recipes import views

urlpatterns = [
    url(r'^$', views.recipe_list.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.recipe_detail.as_view()),
    url(r'^users/(?P<userId>[0-9]+)/$', views.recipeUser_detail.as_view()),
]
