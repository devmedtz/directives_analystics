from django.urls import path

from .import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('school-search-result/', views.school_list, name='school_list'),
    path('subscribe/', views.SubscribeCreateView.as_view(), name='subscribe'),
]