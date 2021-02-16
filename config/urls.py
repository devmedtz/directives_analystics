from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls', namespace='main')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('dashboard/', include('admins.urls', namespace='admins')),
]
