from django.urls import path, include
from django.contrib import admin

handler404 = 'config.views.view_404'

urlpatterns = [

    # admin page
    path('admin/', admin.site.urls),

    # menu app urls
    path('menus/', include('menus.urls')),
]
