from django.urls import path

from .import views

app_name = 'location'

urlpatterns = [
    path('import-region/', views.import_region, name='import_region'),
    path('import-district/', views.import_district, name='import_district'),
    path('ajax/load-district/', views.load_district, name='ajax_load_district'),
]