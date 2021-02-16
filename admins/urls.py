from django.urls import path

from .import views

app_name = 'admins'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create-school/', views.create_edit_school, name='create_school'),
    path('edit-school/<int:id>/', views.create_edit_school, name='edit_school'),
]