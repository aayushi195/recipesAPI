from django.conf.urls import url
from recipes import views

urlpatterns = [
    url(r'^$', views.recipe_list),
    url(r'^(?P<pk>[0-9]+)/$', views.recipe_detail),
   # url('recipesByUser/<int:userId>/', views.recipeUser_detail),
]
