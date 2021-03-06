from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from recipes import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^recipes/', include('recipes.urls')),
    # url('recipes/',views.recipe_list.as_view()),
    # url('recipes/<int:pk>', views.recipe_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)