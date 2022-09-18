from django.urls import path
from . import views

urlpatterns = [
    # path(r'^$', views.post_list, name='post_list'),
    path('articles/2003/', views.current_datetime),
    path('articles/20034/', views.post_list),

]