from django.urls import path

from .import views

app_name = 'admins'

urlpatterns = [
    path('admin/', views.dashboard, name='dashboard'),
    path('create-school/', views.create_edit_school, name='create_school'),
    path('edit-school/<int:id>/', views.create_edit_school, name='edit_school'),
    path('list-schools/', views.list_school, name='list_school'),
    path('school/<int:pk>/delete/', views.SchoolDeleteView.as_view(), name='school_delete'),

    # path('results/<int:school_id>/', views.get_exam_rank, name='results'),

    path('subject-list/', views.SubjectGroupList.as_view(), name='subject_list'),
    path('create-subject/', views.SubjectCreateView.as_view(), name='create_subject'),
    path('update-subject/<int:pk>', views.SubjectUpdateView.as_view(), name='update_subject'),
    path('delete-subject/<int:pk>', views.SubjectDeleteView.as_view(), name='delete_subject'),

    path('combination-list/', views.CombinationList.as_view(), name='combination_list'),
    path('create-combination/', views.CombinationCreateView.as_view(), name='create_combination'),
    path('update-combination/<int:pk>', views.CombinationUpdateView.as_view(), name='update_combination'),
    path('delete-combination/<int:pk>', views.CombinationDeleteView.as_view(), name='delete_combination')
]