from django.urls import path

from .import views

app_name = 'admins'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create-school/', views.create_edit_school, name='create_school'),
    path('edit-school/<int:id>/', views.create_edit_school, name='edit_school'),
    path('list-schools/', views.list_school, name='list_school'),

    path('results/<int:school_id>/', views.get_exam_rank, name='results'),
]